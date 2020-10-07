from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from insta_user.models import InstaUser, UserEmail

admin.site.register(InstaUser, UserAdmin)
admin.site.register(UserEmail)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('bio',)}),


