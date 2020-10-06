from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from insta_user.models import InstaUser

admin.site.register(InstaUser, UserAdmin)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('bio',)}),


