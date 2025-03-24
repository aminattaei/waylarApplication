from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        help_text=(
            "برای ست کردن آیکون، لطفاً نام کلاس آیکون را وارد کنید. "
            "برای مثال: 'fa-solid fa-code' برای FontAwesome یا 'material-icons code' برای Google Icons. "
            "اگر به دنبال آیکون هستید، می‌توانید از لینک‌های زیر استفاده کنید: "
            "<a href='https://fontawesome.com/icons' target='_blank'>FontAwesome</a> یا "
            "<a href='https://material.io/resources/icons/' target='_blank'>Google Icons</a>"
        ),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("سرویس ")
        verbose_name_plural = _("سرویس ها")
