# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='id_game_requested',
            field=models.ForeignKey(to='gt.User_Game', related_name='trades_games_requested'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='id_game_requester',
            field=models.ForeignKey(to='gt.User_Game', related_name='trades_games_requester'),
        ),
    ]
