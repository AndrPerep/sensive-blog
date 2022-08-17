from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']
    raw_id_fields = ['author', 'post']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'tags', 'likes']


admin.site.register(Tag)
