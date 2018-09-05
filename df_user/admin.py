from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['id','uname','upwd','uemail','uphone']

admin.site.register(UserInfo,UserInfoAdmin)