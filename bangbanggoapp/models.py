# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class StuM(models.Model):
    name = models.CharField(u'姓名',max_length=30) 
    password = models.CharField(u'密码',max_length=11)
    address = models.CharField(u'地址',max_length=40)
    stuid = models.CharField(u'学号',max_length=12,primary_key = True)
    phonenum = models.CharField(u'手机号码',max_length=11)
    stuscore = models.IntegerField(u'荣誉值',default=20)
    def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.stuid

class SendPackage(models.Model):
    SADRESS = (
        ('行建轩一栋','行建轩一栋'),
        ('行建轩二栋','行建轩二栋'),
        ('行建轩三栋','行建轩三栋'),
        ('行建轩四栋','行建轩四栋'),
        ('行建轩五栋','行建轩五栋'),
        ('行建轩六栋','行建轩六栋'),
        ('至诚轩一栋','至诚轩一栋'),
        ('至诚轩二栋','至诚轩二栋'),
        ('至诚轩三栋','至诚轩三栋'),
        ('至诚轩四栋','至诚轩四栋'),
        ('弘毅轩一栋','弘毅轩一栋'),
        ('弘毅轩二栋','弘毅轩二栋'),
        ('弘毅轩三栋','弘毅轩三栋'),
        ('弘毅轩四栋','弘毅轩四栋'),
        ('敏行轩','敏行轩')
    )
    SETYPE=(
        ('fs','服饰'),
        ('jj','家具'),
        ('dq','电器'),
        ('mz','美妆护肤'),
        ('ts','图书'),
        ('lx','旅行'),
    )
    stuid = models.CharField(u'学号',max_length=12)
    sname = models.CharField(u'收件人姓名:',max_length=30)
    saddress = models.CharField(u'住址:',max_length=10,choices=SADRESS)
    sexpressad = models.CharField(u'快递名称:',max_length=30)
    sename = models.CharField(u'提取码:',max_length=15)
    sphone = models.CharField(u'联系方式:',max_length=11)
    setype = models.CharField(u'快递类型:',max_length=2,choices=SETYPE,default=u'服饰')
    sflag = models.IntegerField(u'是否接单:',default=0)
    stuidhelp = models.CharField(u'接单人',max_length=12,default='0')
    class Meta:
        unique_together = ('sname','saddress','sexpressad','sename','sphone','setype')
    def __unicode__(self):
        return self.sname

class Chat(models.Model):
    sender = models.ForeignKey(StuM,related_name='stuidname')
    content = models.TextField()
    ctime = models.DateTimeField(auto_now_add=True,null = True)

    def __unicode__(self):
        return u'%s' % self.content
