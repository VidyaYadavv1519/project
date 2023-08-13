from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.filter()
    serializer_class = ProjectSerializer
    