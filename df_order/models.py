#coding=utf-8
from django.db import models


#订单的主表
class OrderInfo(models.Model):
	oid=models.CharField(max_length=20, primary_key=True,verbose_name='订单编号')  #订单的编号
	user=models.ForeignKey('df_user.UserInfo',verbose_name='引用自用户注册表') #那个人下的订单
	odate=models.DateTimeField(auto_now=True,verbose_name='下单日期') #下订单的日期,当前时间
	oIsPay=models.BooleanField(default=False,verbose_name='支付方式') #是否支付
	ototal=models.DecimalField(max_digits=6,decimal_places=2,verbose_name='总金额') #总计　总金额
	oaddress=models.CharField(max_length=150,default='',verbose_name='收货地址') #地址


	def __str__(self):
		return self.oid

	class Meta:
		verbose_name = '订单总表'
		verbose_name_plural = verbose_name






#订单的详表
class OrderDetailInfo(models.Model):
	goods=models.ForeignKey('df_goods.GoodsInfo',verbose_name='引用自商品类')
	order=models.ForeignKey('OrderInfo',verbose_name='引用自订单主表') #和订单主表关连
	price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='商品价格') #价格
	count=models.IntegerField(verbose_name='数量') #数量



	class Meat:
		verbose_name = '订单详表'
		verbose_name_plural = verbose_name

