#coding=utf-8
from django.db import models


#购物车
class CartInfo(models.Model):
	user=models.ForeignKey('df_user.UserInfo',verbose_name='用户') #用户,关系用户模型类
	goods=models.ForeignKey('df_goods.GoodsInfo',verbose_name='商品') #商品，关联商品模型类
	count=models.IntegerField(verbose_name='数量') #数量


	def __str__(self):
		return self.user


	class Meta:
		verbose_name = "购物车"
		verbose_name_plural = verbose_name
