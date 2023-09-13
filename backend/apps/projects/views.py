from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
