from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published', 'created', 'updated']
    list_filter = ['published', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}