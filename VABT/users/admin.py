from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

class ChapterInline(admin.StackedInline):
    model = Chapter
    can_delete = False
    verbose_name_plural = 'chapter'

class UserAdmin(BaseUserAdmin):
    inlines = (ChapterInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)