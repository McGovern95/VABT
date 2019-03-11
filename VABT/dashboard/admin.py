from django.contrib import admin
import site
from django.conf.urls import url
from .models import Post
# Register your models here.
admin.site.register(Post)
admin.site.site_title = 'VABT admin'
admin.site.site_header = 'VABT Administration'
admin.site.index_title = ''
