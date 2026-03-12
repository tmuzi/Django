from snippetsfive.models import Snippet
from django.contrib.auth.models import User
from snippetsfive.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from snippetsfive.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response


# 5 - Relationships and hyperlinked APIs
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

# 4 - Authentication and Permissions
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # If we created a code snippet,
    # there'd be no way of associating the user that created the snippet,
    # with the snippet instance.
    # The user isn't sent as part of the serialized representation,
    # but is instead a property of the incoming request.
    # The way we deal with that is by overriding
    # a .perform_create() method on our snippet views,
    # that allows us to modify how the instance save is managed,
    # and handle any information that is implicit in the incoming request or requested URL.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

