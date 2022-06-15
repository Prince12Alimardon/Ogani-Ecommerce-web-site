from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'created_at')
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
