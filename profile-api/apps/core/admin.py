from django.contrib import admin
from core.models import Profile

# Register your models here.

class UsersProfile(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'age', 'sex')
    list_display_links = ('id', 'firstName')
    search_fields = ('nome',)

admin.site.register(Profile, UsersProfile)

