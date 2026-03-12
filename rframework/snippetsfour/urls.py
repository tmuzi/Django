from django.urls import path
from snippetsfour import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/v4/", views.SnippetList.as_view()),
    path("snippets/v4/<int:pk>/", views.SnippetDetail.as_view()),

    # 4 - Authentication and Permissions (for some reason v4/ is not working)
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)