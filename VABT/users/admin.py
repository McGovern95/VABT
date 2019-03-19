from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class UserExtendedInline(admin.StackedInline):
    model = UserExtended
    can_delete = True
    verbose_name_plural = 'Extra Student Configuration'

class UserAdmin(BaseUserAdmin):
    inlines = (UserExtendedInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)