from django.contrib import admin
from .models import Blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = "__all__"




