# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import StuM,SendPackage,Chat

# from bangbanggoapp import models

class StuMAdmin(admin.ModelAdmin):
    list_display = ('name','password','stuid','phonenum',)

admin.site.register(StuM,StuMAdmin)

class SendPackageAdmin(admin.ModelAdmin):
    list_display = ('stuid','sname','sexpressad','sename','sphone','setype','sflag')

admin.site.register(SendPackage,SendPackageAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender','content','ctime')

admin.site.register(Chat,ChatAdmin)
