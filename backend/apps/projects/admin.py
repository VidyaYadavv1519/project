from django.contrib import admin
from .models import Project, Tag, Review, ProjectMember


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(ProjectMember)
