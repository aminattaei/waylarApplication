from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"
