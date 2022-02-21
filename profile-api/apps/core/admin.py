from django.contrib import admin
from core.models import Profile

# Register your models here.

class UsersProfile(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'sex')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name',)

admin.site.register(Profile, UsersProfile)

