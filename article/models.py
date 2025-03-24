from django.db import models
from django.utils.translation import gettext as _


class Blog(models.Model):
    categories = models.OneToOneField(
        "Category",
        verbose_name=_("دسته بندی"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(_("عنوان مقاله"), max_length=50)
    created_time = models.DateField(_("تاریخ ایجاد مقاله "), auto_now_add=True)
    image = models.ImageField(_("تصویر مقاله"), upload_to="article/", null=True)
    content = models.TextField(_("متن مقاله"))

    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقالات")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Blog_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    title = models.CharField(_("عنوان دسته بندی"), max_length=50)
    description = models.TextField(_("توضیح دسته بندی"))

    class Meta:
        verbose_name = _("دسته")
        verbose_name_plural = _("دسته ها")

    def __str__(self):
        return self.title