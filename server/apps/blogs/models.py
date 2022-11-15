from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from apps.profiles.models import Profile


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)

    title = models.CharField(_("title"), max_length=60)
    body = RichTextField(_("body"))
    created_at = models.DateTimeField(_("date uploaded"), auto_now_add=True)
    updated_at = models.DateTimeField(_("date edited"), auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class BlogAssets(models.Model):
    file = models.ImageField(upload_to="blogs/assets/")

    class Meta:
        verbose_name = _("blog assets")
        verbose_name_plural = _("blog assets")
