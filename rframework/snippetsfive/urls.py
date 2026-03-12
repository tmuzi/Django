from django.urls import path
from snippetsfive import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/v5/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/v5/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),

    # 4 - Authentication and Permissions (for some reason v4/ is not working)
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),

    # 5 - Relationships and hyperlinked APIs
    path("", views.api_root),
    path("snippets/v5/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)