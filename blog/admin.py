from django.contrib import admin
from .models import Post

admin.site.register(Post)


class PostModelAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'date_posted', 'autor']
