from django.contrib import admin
from .models import Post, Category, Tag, Music, FriendLink

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'view_count',
                    'create_time', 'update_time', 'can_comment',
                    'pin', 'draft', 'hide')
    list_display_links = ['id', 'title', 'category']
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': (('title', 'author',
                        'show_desc', 'cc'),
                       ('category', 'tag', 'toc'),
                       'music',
                       'desc',
                       'body')
        }),
        ('Options', {
            'classes': ('collapse',),
            'fields': (('hide', 'pin', 'draft',
                        'can_comment'),
                       'create_time')
        })
    )
    search_fields = ['title', 'create_time', 'draft',
                     'hide', 'pin']
    list_filter = ['category__name', 'create_time']
    date_hierarchy = 'create_time'
    ordering = ['-create_time']
    list_editable = ['can_comment', 'hide', 'draft', 'pin']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Music)
admin.site.register(FriendLink)
