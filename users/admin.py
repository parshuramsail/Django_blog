from django.contrib import admin
from .models import Profile

admin.site.register(Profile)


class ProfileModelAdmin(admin.ModelAdmin):
    fields = ['user', 'image']
