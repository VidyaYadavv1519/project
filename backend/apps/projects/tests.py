from django.test import TestCase               # noqa: F401
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User  # Import your User model if it's different

from .models import Project  # Import your Project model if it's in a different location
from .serializers import ProjectSerializer

class ProjectAPITest(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create some test projects
        self.project1 = Project.objects.create(
            title="Project 1",
            description="Description 1",
            creator=self.user,
        )
        self.project2 = Project.objects.create(
            title="Project 2",
            description="Description 2",
            creator=self.user,
        )

        # Initialize the API client
        self.client = APIClient()

    def test_unauthenticated_access_to_api(self):
        # Test unauthenticated access to the /api/ endpoint
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test unauthenticated access to the /api/<int> endpoint
        response = self.client.get(f'/api/{self.project1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_access_to_api(self):
        # Authenticate the client with the test user
        self.client.force_authenticate(user=self.user)

        # Test authenticated access to the /api/ endpoint
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test authenticated access to the /api/<int> endpoint
        response = self.client.get(f'/api/{self.project1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_project_serializer(self):
        # Create a project serializer instance
        serializer = ProjectSerializer(instance=self.project1)
        
        # Check that the serialized data matches the expected structure
        expected_data = {
            'id': str(self.project1.id),
            'created_at': serializer.data['created_at'],  # You can compare timestamps or ignore them
            'updated_at': serializer.data['updated_at'],
            'creator': self.user.id,  # Replace with the actual user ID
            'title': 'Project 1',
            'description': 'Description 1',
            'private': False,  # You can update this if needed
            'tags': [],
            'reviews': [],
            'topics': [],
        }
        self.assertEqual(serializer.data, expected_data)


# Create your tests here.
