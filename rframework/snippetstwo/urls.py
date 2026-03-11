from django.urls import path
from snippetstwo import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/v2/", views.snippet_list),
    path("snippets/v2/<int:pk>/", views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)