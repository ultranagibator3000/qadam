from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(
        _("profile image"), upload_to="profile/", blank=True, null=True)

    about = RichTextField(_("about me"), blank=True)
    social_media = RichTextField(_("social media links"), blank=True)

    contacts = RichTextField(_("contacts"), blank=True)
    skills = RichTextField(_("skills"), blank=True)


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    name = models.CharField(max_length=60)
    body = RichTextField(_("body"))
    from_date = models.DateField(_("from date"))
    to_date = models.DateField(_("to date"), auto_now=True)
