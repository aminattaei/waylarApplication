from django.db import models
from django.utils.translation import gettext as _


class ContactUs(models.Model):
    title = models.CharField(_("موضوع"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    content = models.TextField(_("متن"))

    class Meta:
        verbose_name = _("ارتباط")
        verbose_name_plural = _("ارتباطات")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("ContactUs_detail", kwargs={"pk": self.pk})
