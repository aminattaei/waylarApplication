from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'is_approved','created_at')
    list_filter = ['is_approved','created_at']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "کامنت‌های انتخاب‌شده تأیید شدند.")
    
    approve_comments.short_description = "تأیید کامنت‌های انتخاب‌شده"

admin.site.register(Comment, CommentAdmin)
