from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'views_count',)
    list_filter = ('views_count',)
    search_fields = ('title', 'content',)
