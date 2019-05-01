from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
from dashboard.models import Post
# Register your models here.

#class PostInline(admin.StackedInline):
#    model = Post
#    can_delete = True
#    verbose_name_plural = 'Certification Configuration'


class UserExtendedInline(admin.StackedInline):
    model = UserExtended
    can_delete = True
    verbose_name_plural = 'Extra Student Configuration'

class UserAdmin(BaseUserAdmin):
    inlines = (UserExtendedInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(UserExtended)
admin.site.register(Post)
admin.site.site_title = 'VABT admin'
admin.site.site_header = 'VABT Administration'
admin.site.index_title = ''
