from django.urls import path
from snippetsthree import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/v3/", views.SnippetListThree.as_view()),
    path("snippets/v3/<int:pk>/", views.SnippetDetailThree.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)