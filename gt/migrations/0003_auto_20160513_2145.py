# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gt.models


class Migration(migrations.Migration):

    dependencies = [
        ('gt', '0002_remove_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=30, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='address',
            name='uf',
            field=models.CharField(max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='users',
            name='picture',
            field=models.ImageField(upload_to=gt.models.upload_to_user, default='/static/images/UserDefault.png', blank=True, verbose_name='Imagem', null=True),
        ),
    ]
