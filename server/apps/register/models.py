from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationForm(models.Model):
    name = models.CharField(_("name"), max_length=60)
    contacts = models.CharField("contact", max_length=11) 
