# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('msg_started', models.TextField()),
                ('msg_accepted', models.TextField()),
                ('msg_finished', models.TextField()),
                ('date_started', models.DateField()),
                ('date_accepted', models.DateField()),
                ('date_finished', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Consoles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('picture', models.ImageField(upload_to='', default='')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('kind', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_Console',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('id_console', models.ForeignKey(to='gt.Consoles')),
            ],
        ),
        migrations.CreateModel(
            name='Game_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('picture', models.ImageField(upload_to='', default='')),
                ('description', models.CharField(max_length=300)),
                ('id_console', models.ForeignKey(to='gt.Consoles')),
                ('id_dev', models.ForeignKey(to='gt.Developers')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trade_Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_requester_status', models.BooleanField()),
                ('user_requested_status', models.BooleanField()),
                ('date', models.DateField()),
                ('id_game_requested', models.ForeignKey(to='gt.Games', related_name='trades_games_requested')),
                ('id_game_requester', models.ForeignKey(to='gt.Games', related_name='trades_games_requester')),
                ('id_status', models.ForeignKey(to='gt.Status')),
                ('id_trade_kind', models.ForeignKey(to='gt.Trade_Kind')),
            ],
        ),
        migrations.CreateModel(
            name='User_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('id_game', models.ForeignKey(to='gt.Games')),
            ],
        ),
        migrations.CreateModel(
            name='User_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=2)),
                ('id_trade', models.ForeignKey(to='gt.Trades')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.IntegerField()),
                ('picture', models.ImageField(upload_to='', default='')),
            ],
        ),
        migrations.AddField(
            model_name='user_rating',
            name='id_user',
            field=models.ForeignKey(to='gt.Users'),
        ),
        migrations.AddField(
            model_name='user_game',
            name='id_user',
            field=models.ForeignKey(to='gt.Users'),
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requested',
            field=models.ForeignKey(to='gt.Users', related_name='trades_user_requested'),
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requester',
            field=models.ForeignKey(to='gt.Users', related_name='trades_users_requester'),
        ),
        migrations.AddField(
            model_name='games',
            name='id_genre',
            field=models.ForeignKey(to='gt.Genres'),
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_game',
            field=models.ForeignKey(to='gt.Games'),
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_user',
            field=models.ForeignKey(to='gt.Users'),
        ),
        migrations.AddField(
            model_name='game_console',
            name='id_game',
            field=models.ForeignKey(to='gt.Games'),
        ),
        migrations.AddField(
            model_name='consoles',
            name='id_dev',
            field=models.ForeignKey(to='gt.Developers'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_trade',
            field=models.ForeignKey(to='gt.Trades'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_user_requested',
            field=models.ForeignKey(to='gt.Users', related_name='chat_users_requested'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_user_requester',
            field=models.ForeignKey(to='gt.Users', related_name='chat_users_requester'),
        ),
        migrations.AddField(
            model_name='address',
            name='id_user',
            field=models.ForeignKey(to='gt.Users'),
        ),
    ]
