from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Project, Category
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


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "projects/single-project.html"
    context_object_name = "project"
    model = Project


class ProjectListApiViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class Create_new_project(LoginRequiredMixin, generic.CreateView):
    template_name = "projects/create_new_project.html"
    model = Project
    success_url = reverse_lazy("projects_list")
    fields = [
        "title",
        "image",
        "area",
        "infrastructure",
        "Financial_value",
        "Project_location",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        categories_data = self.request.POST.getlist("categories")  #
        category_instances = []
        for cat in categories_data:
            if cat.startswith("new-"):
                new_category, created = Category.objects.get_or_create(name=cat[4:])
                category_instances.append(new_category)
            else:
                category_instances.append(Category.objects.get(id=cat))

        self.object.categories.set(category_instances)
        return response
