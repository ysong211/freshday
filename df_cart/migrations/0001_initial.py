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
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField(verbose_name='数量')),
                ('goods', models.ForeignKey(verbose_name='商品', to='df_goods.GoodsInfo')),
                ('user', models.ForeignKey(verbose_name='用户', to='df_user.UserInfo')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
