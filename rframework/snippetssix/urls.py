from django.urls import path
from snippetssix.views import api_root, SnippetViewSet, UserViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

# 6 - Viewsets and routers
snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
    )
snippet_highlight = SnippetViewSet.as_view({"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path("", api_root),
    path("snippets/v6/", snippet_list, name="snippet-list"),
    path("snippets/v6/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("snippets/v6/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),

    # 4 - Authentication and Permissions (for some reason v4/ is not working)
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)