from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from django.utils.translation import gettext_lazy as _


class PermissionsType(models.TextChoices):
    ADMIN= "ADMIN", _("ADMIN")
    STANDARD = "STANDARD", _("STANDARD")
"""
place holder until more specific permissions identified
"""

class Tag(models.Model):
    name = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], blank=False
    )

    def __str__(self):
        return str(self.reviewer) + " | " + str(self.rating)


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, blank=False)
    description = models.CharField(max_length=200)
    private = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.title + " | " + str(self.creator)

class ProjectMember(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.USER_AUTH_MODEL, on_delete=models.CASCADE, blank=True)
    permissions = models.CharField(max_length= 10, choices=PermissionsType)
    """
    can be a boolean field
    """
