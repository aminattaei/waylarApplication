from django.shortcuts import render
from django.views import generic
from .models import Project,ProjectEngineer
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from django.core.cache import cache

from .serializers import ProjectSerializer


def blacklist_token(token):
    cache.set(f"blacklisted_{token}", True, timeout=60 * 60 * 24)


def is_token_blacklisted(token):
    return cache.get(f"blacklisted_{token}")


class ProjectListView(generic.ListView):
    template_name = "projects/project.html"
    model = Project
    context_object_name = "projects"


class ProjectDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "projects/single-project.html"
    context_object_name = "project"
    model = Project


class ProjectListApiViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


def ProjectEngineerDetail(request):
    pass