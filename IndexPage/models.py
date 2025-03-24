from django.db import models
from django.utils.translation import gettext as _


class NewsPaper(models.Model):
    email = models.EmailField(_("ایمیل"), max_length=254)

    class Meta:
        verbose_name = _("خبرنامه")
        verbose_name_plural = _("خبرنامه ها")

    def __str__(self):
        return self.email
