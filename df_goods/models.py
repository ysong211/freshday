#coding=utf-8

from django.db import models

#副文本编辑器
from tinymce.models import HTMLField


#商品的分类
class TypeInfo(models.Model):
	ttitle=models.CharField(max_length=20,verbose_name='商品类名') #商品类名
	isDelete=models.BooleanField(default=False,verbose_name='激活状态') #逻辑删除

	def  __str__(self):
		return '%s'%self.ttitle


	class Meta:
		verbose_name = '商品种类'
		verbose_name_plural = verbose_name




#商品类
class GoodsInfo(models.Model):
	gtitle=models.CharField(max_length=20,verbose_name='商品名称') #名字
	gpic=models.ImageField(upload_to='goods/',verbose_name='图片') #图片
	gprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格') #价格 5位，２位小数
	isDelete=models.BooleanField(default=False,verbose_name='激活状态') #默认不删除
	gunit=models.CharField(max_length=20,default='500g',verbose_name='商品单位') #单位
	gclick=models.IntegerField(verbose_name='销售量')  #点击点,人气,销量
	gjianjie=models.CharField(max_length=200,verbose_name='商品简介') #简介
	gkucun=models.IntegerField(verbose_name='购买数量') #库存，购买的数量
	gcontent=HTMLField(verbose_name='商品详情') #详情简介,商品详情
	gtype=models.ForeignKey(TypeInfo,verbose_name='引用自商品总类') #外键关联

	def  __str__(self):
		return '%s'%self.gtitle


	class Meta:
		verbose_name = '商品类'
		verbose_name_plural = verbose_name

