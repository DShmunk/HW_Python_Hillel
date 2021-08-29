# Register your models here.

from django.contrib import admin
from .models import Post, Comment
 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_by', 'publish_at', 'status')
    list_filter = ('status', 'created_at', 'publish_at', 'created_by')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('created_by',)
    date_hierarchy = 'publish_at'
    ordering = ['status', 'publish_at']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
