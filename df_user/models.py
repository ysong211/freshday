#coding=utf-8
from django.db import models


#用户注册信息
class UserInfo(models.Model):
	uname = models.CharField(max_length=20,verbose_name='用户名') #用户名
	upwd = models.CharField (max_length=40,verbose_name='密码') #密码
	uemail = models.CharField(max_length=30,verbose_name='邮箱') #邮箱
	ushouuser = models.CharField(max_length=20,default='',verbose_name='收件人') #收件人并设置默认值
	uaddress = models.CharField(max_length=100,default='',verbose_name='详细地址') #详细地址
	uyoubian = models.CharField(max_length=6,default='',verbose_name='邮编') #邮编
	uphone = models.CharField(max_length=11,default='',verbose_name='手机号码') #手机号码
    #default,blank 是python层面的约束，不影响数据库表结构

	def __str__(self):
		return self.uname.encode('utf-8')


	class Meta:
		verbose_name = '用户注册表'
		verbose_name_plural = verbose_name