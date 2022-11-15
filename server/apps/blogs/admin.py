from django.contrib import admin

from apps.blogs.models import Blog, BlogAssets


@admin.register(Blog, BlogAssets)
class BlogAdmin(admin.ModelAdmin):
    pass
