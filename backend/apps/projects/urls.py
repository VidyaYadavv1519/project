from django.contrib import admin
from django.urls import path
from .views import ProjectList, ProjectDetail

app_name = "projects"

urlpatterns = [
    path("<int:pk>/", ProjectDetail.as_view(), name="project-detail"),
    path("", ProjectList.as_view(), name="project-list"),
]
