# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gt', '0003_auto_20160513_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_game',
            old_name='want_have',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(blank=True, verbose_name='Nº', null=True),
        ),
    ]
