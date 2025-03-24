from django.db import models
from django.utils.translation import gettext as _


class Project(models.Model):
    categories = models.ManyToManyField(
        "Category", verbose_name=_("دسته پروژه"), blank=True
    )
    title = models.CharField(_("عنوان پروژه"), max_length=50)
    created_time = models.DateField(_("تاریخ ایجاد پروژه "), auto_now_add=True)
    image = models.ImageField(_("تصویر پروژه"), upload_to="projects/", null=True)
    area = models.CharField(_("مساحت پروژه"), max_length=50)
    start_time = models.DateTimeField(_("زمان شروع"), auto_now=True, auto_now_add=False)
    infrastructure = models.IntegerField(_("زیربنا"), default=0)
    Financial_value = models.IntegerField(_("ارزش مالی"))
    Project_location = models.CharField(_("مکان پروژه"), max_length=50)

    content = models.TextField(_("متن پروژه"))

    class Meta:
        verbose_name = _("پروژه ")
        verbose_name_plural = _("پروژه ها")

    def __str__(self):
        return f"Project title: {self.title}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("Project_detail", kwargs={"pk": self.pk})


class ProjectEngineer(models.Model):
    post = models.OneToOneField(Project, on_delete=models.CASCADE)
    name = models.CharField(_("نام مهندس"), max_length=50)
    Occupation = models.CharField(_("رسته شغلی"), max_length=50, default="مهندس عمران")
    image = models.ImageField(_("تصویر مهندس"), upload_to="ProjectEngineer/")

    def __str__(self):
        return f"Project engineer name: {self.name}"

    class Meta:
        verbose_name = _("مهندس ")
        verbose_name_plural = _("مهندسین")


class Category(models.Model):
    title = models.CharField(_("عنوان دسته بندی"), max_length=50)
    description = models.TextField(_("توضیح دسته بندی"))
