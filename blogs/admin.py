from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'author')
    list_filter = ('date_added', 'author')
    search_fields = ('title', 'text')
