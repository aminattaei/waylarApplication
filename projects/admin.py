from django.contrib import admin
from .models import Project, ProjectEngineer, Category


admin.site.register(Project)
admin.site.register(ProjectEngineer)
admin.site.register(Category)
