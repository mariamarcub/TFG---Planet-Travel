from django.contrib import admin
from forum.models import VoyageThread, Comment


@admin.register(VoyageThread)
class VoyageThreadAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created_date', 'created_by', 'voyage']
    list_display = ['title','voyage']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['client', 'content']
    list_display = ['content']