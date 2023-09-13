from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "projects"

router = DefaultRouter()
router.register(r"projects", views.ProjectView, basename="projects")

urlpatterns = [path("", include(router.urls))]
