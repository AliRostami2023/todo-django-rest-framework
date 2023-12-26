from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'email', 'is_superuser']


admin.site.unregister(Group)