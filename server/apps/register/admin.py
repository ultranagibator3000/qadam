from django.contrib import admin

from apps.register.models import ApplicationForm


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    pass
