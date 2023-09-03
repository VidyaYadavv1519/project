from django.urls import path

from .views import project_detail, project_list

app_name = "projects"

urlpatterns = [
    path("<int:pk>/", project_detail, name="project-detail"),
    path("", project_list, name="project-list"),
]
