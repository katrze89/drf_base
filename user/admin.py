from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User

class CustomUser(UserAdmin):
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', "confirm_account")

admin.site.register(User, UserAdmin)
