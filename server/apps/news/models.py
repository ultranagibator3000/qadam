from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(_("title"), max_length=60)
    body = RichTextField(_("body"))
    image = models.ImageField(_("image"), upload_to="news/images/")

    created_at = models.DateTimeField(_("date uploaded"), auto_now_add=True)
    updated_at = models.DateTimeField(_("date edited"), auto_now=True)

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")
        ordering = ["-created_at", "-updated_at"]
