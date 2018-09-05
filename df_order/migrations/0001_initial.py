# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=5, decimal_places=2)),
                ('count', models.IntegerField(verbose_name='数量')),
                ('goods', models.ForeignKey(verbose_name='引用自商品类', to='df_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(verbose_name='订单编号', primary_key=True, max_length=20, serialize=False)),
                ('odate', models.DateTimeField(verbose_name='下单日期', auto_now=True)),
                ('oIsPay', models.BooleanField(verbose_name='支付方式', default=False)),
                ('ototal', models.DecimalField(verbose_name='总金额', max_digits=6, decimal_places=2)),
                ('oaddress', models.CharField(verbose_name='收货地址', max_length=150, default='')),
                ('user', models.ForeignKey(verbose_name='引用自用户注册表', to='df_user.UserInfo')),
            ],
            options={
                'verbose_name': '订单总表',
                'verbose_name_plural': '订单总表',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(verbose_name='引用自订单主表', to='df_order.OrderInfo'),
        ),
    ]
