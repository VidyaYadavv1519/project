from rest_framework import serializers
from .models import Project, ProjectMember


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "created_at",
            "updated_at",
            "creator",
            "title",
            "description",
            "private",
            "tags",
            "topics",
        ]


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "creator",
            "title",
            "description",
            "private",
            "tags",
            "topics",
        ]


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [
            "id",
            "user",
            "updated_at",
            "project",
        ]