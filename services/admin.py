from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service
        fields = "__all__"
