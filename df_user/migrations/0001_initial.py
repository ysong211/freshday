# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(verbose_name='用户名', max_length=20)),
                ('upwd', models.CharField(verbose_name='密码', max_length=40)),
                ('uemail', models.CharField(verbose_name='邮箱', max_length=30)),
                ('ushouuser', models.CharField(verbose_name='收件人', max_length=20, default='')),
                ('uaddress', models.CharField(verbose_name='详细地址', max_length=100, default='')),
                ('uyoubian', models.CharField(verbose_name='邮编', max_length=6, default='')),
                ('uphone', models.CharField(verbose_name='手机号码', max_length=11, default='')),
            ],
            options={
                'verbose_name': '用户注册表',
                'verbose_name_plural': '用户注册表',
            },
        ),
    ]
