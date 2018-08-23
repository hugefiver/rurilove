from django.contrib import admin
from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'create_time', 'hide']
    list_display_links = ['name', 'post']
    list_filter = ['name', 'create_time']
    search_fields = ['name', 'post__id',
                     'post__title', 'create_time']
    list_editable = ['hide']
    list_per_page = 30
    date_hierarchy = 'create_time'
    fields = (('name', 'post', 'hide'),
              'url',
              'email',
              'body')

