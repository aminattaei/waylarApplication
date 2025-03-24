from django.shortcuts import render
from .models import Service
from django.views import generic

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ServiceSerializer


class ServicesListView(generic.ListView):
    model = Service
    context_object_name = "Services"
    template_name = "services/services.html"


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
