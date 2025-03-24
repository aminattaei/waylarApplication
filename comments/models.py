from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from article.models import Blog


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("نویسنده"), on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Blog,
        verbose_name=_("مقاله"),
        on_delete=models.CASCADE,
        null=True,
        related_name="comments",
    )
    job = models.CharField(_("حرفه"), max_length=50, default="مشتری", blank=True)
    content = models.TextField(_("متن نظر"))
    image = models.ImageField(
        _("تصویر کاربر"),
        upload_to="comment_users_image/",
        default="templates/default-avatar.jpg",
        blank=True,
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        _("زمان ایجاد"), auto_now=False, auto_now_add=True
    )

    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")

    def __str__(self):
        return f"{self.author} - {self.content[:30]}"
