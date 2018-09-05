# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(verbose_name='商品名称', max_length=20)),
                ('gpic', models.ImageField(verbose_name='图片', upload_to='goods')),
                ('gprice', models.DecimalField(verbose_name='价格', max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(verbose_name='激活状态', default=False)),
                ('gunit', models.CharField(verbose_name='商品单位', max_length=20, default='500g')),
                ('gclick', models.IntegerField(verbose_name='销售量')),
                ('gjianjie', models.CharField(verbose_name='商品简介', max_length=200)),
                ('gkucun', models.IntegerField(verbose_name='购买数量')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='商品详情')),
            ],
            options={
                'verbose_name': '商品类',
                'verbose_name_plural': '商品类',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ttitle', models.CharField(verbose_name='商品类名', max_length=20)),
                ('isDelete', models.BooleanField(verbose_name='激活状态', default=False)),
            ],
            options={
                'verbose_name': '商品种类',
                'verbose_name_plural': '商品种类',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(verbose_name='引用自商品总类', to='df_goods.TypeInfo'),
        ),
    ]
