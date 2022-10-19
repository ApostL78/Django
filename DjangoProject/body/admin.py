from django.contrib import admin
from .models import Task, Categories


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('is_published', 'category')
    list_filter = ('category', 'created_at', 'is_published')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Task, TaskAdmin)
admin.site.register(Categories, CategoriesAdmin)
