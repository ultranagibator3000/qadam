from django.contrib import admin

from apps.profiles.models import Profile, Experience


@admin.register(Profile, Experience)
class ProfileAdmin(admin.ModelAdmin):
    pass 
