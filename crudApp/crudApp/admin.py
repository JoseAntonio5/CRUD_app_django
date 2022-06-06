from django.contrib import admin
from .models import PostModel

# admin.site.register(PostModel)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'posted_at')
    search_fields = ['title', 'description']

admin.site.register(PostModel, PostModelAdmin)