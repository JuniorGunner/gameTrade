# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
<<<<<<< HEAD
import gt.models
from django.conf import settings
=======
from django.conf import settings
import gt.models
>>>>>>> origin/master


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=30)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('street', models.CharField(blank=True, verbose_name='Rua', max_length=200)),
                ('number', models.IntegerField(blank=True, verbose_name='Nº')),
                ('complement', models.CharField(blank=True, verbose_name='Complemento', max_length=30)),
                ('district', models.CharField(blank=True, verbose_name='Bairro', max_length=50)),
                ('zip_code', models.CharField(blank=True, verbose_name='CEP', max_length=9)),
                ('city', models.CharField(blank=True, verbose_name='Cidade', max_length=50)),
                ('uf', models.CharField(blank=True, verbose_name='UF', max_length=2)),
                ('country', models.CharField(blank=True, verbose_name='País', max_length=30)),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_started', models.TextField()),
                ('msg_accepted', models.TextField()),
                ('msg_finished', models.TextField()),
                ('date_started', models.DateField()),
                ('date_accepted', models.DateField()),
                ('date_finished', models.DateField()),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('msg_started', models.TextField(blank=True, verbose_name='Mensagem Inicial')),
                ('msg_accepted', models.TextField(blank=True, verbose_name='Mensagem de Aceitação')),
                ('msg_finished', models.TextField(blank=True, verbose_name='Mensagem de Conclusão')),
                ('date_started', models.DateField(auto_now_add=True, null=True, verbose_name='Data Primeira Mensagem')),
                ('date_updated', models.DateField(auto_now=True, null=True, verbose_name='Data de Atualização')),
                ('date_finished', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Consoles',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('picture', models.ImageField(upload_to=gt.models.upload_to_console, default='')),
                ('description', models.CharField(max_length=300)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Ano')),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_console)),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, verbose_name='Nome', max_length=100)),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Game_Console',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=gt.models.upload_to_game, default='')),
                ('id_console', models.ForeignKey(to='gt.Consoles')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_game)),
                ('id_console', models.ForeignKey(verbose_name='Console', to='gt.Consoles')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Game_Rating',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=2)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.DecimalField(max_digits=4, verbose_name='Avaliação do Jogo', decimal_places=2)),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('id_dev', models.ForeignKey(to='gt.Developers')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Ano')),
                ('description', models.TextField(blank=True, verbose_name='Descrição', max_length=300)),
                ('id_dev', models.ForeignKey(verbose_name='Desenvolvedor', to='gt.Developers')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
>>>>>>> origin/master
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('group', models.CharField(verbose_name='Grupo', max_length=100)),
                ('description', models.CharField(verbose_name='Descrição', max_length=200)),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_requester_status', models.BooleanField()),
                ('user_requested_status', models.BooleanField()),
                ('date', models.DateField()),
                ('id_game_requested', models.ForeignKey(related_name='trades_games_requested', to='gt.Games')),
                ('id_game_requester', models.ForeignKey(related_name='trades_games_requester', to='gt.Games')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_requester_status', models.BooleanField(verbose_name='Status Requisitante')),
                ('user_requested_status', models.BooleanField(verbose_name='Status Requisitado')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data da Troca')),
                ('id_game_requested', models.ForeignKey(related_name='trades_games_requested', verbose_name='Jogo Requisitado', to='gt.Games')),
                ('id_game_requester', models.ForeignKey(related_name='trades_games_requester', verbose_name='Jogo Requisitante', to='gt.Games')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='User_Game',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_game_console', models.ForeignKey(to='gt.Game_Console')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('id_game_console', models.ForeignKey(verbose_name='Jogo/Console', to='gt.Game_Console')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='User_Rating',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=2)),
                ('id_trade', models.ForeignKey(to='gt.Trades')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.DecimalField(max_digits=4, verbose_name='Avaliação do Usuário', decimal_places=2)),
                ('id_trade', models.ForeignKey(verbose_name='Troca', to='gt.Trades')),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=gt.models.upload_to_user, default='')),
                ('address', models.OneToOneField(to='gt.Address')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_user)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254)),
                ('address', models.OneToOneField(verbose_name='Endereço', to='gt.Address')),
                ('user', models.OneToOneField(verbose_name='Usuário', to=settings.AUTH_USER_MODEL)),
>>>>>>> origin/master
            ],
        ),
        migrations.AddField(
            model_name='user_rating',
            name='id_user',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Users'),
=======
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='user_game',
            name='id_user',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Users'),
        ),
        migrations.AddField(
            model_name='user_game',
            name='rating',
            field=models.ForeignKey(to='gt.Kind'),
=======
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='user_game',
            name='want_have',
            field=models.ForeignKey(verbose_name='Quero/Tenho', to='gt.Kind'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requested',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='trades_user_requested', to='gt.Users'),
=======
            field=models.ForeignKey(related_name='trades_user_requested', verbose_name='User Requisitado', to='gt.Users'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requester',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='trades_users_requester', to='gt.Users'),
=======
            field=models.ForeignKey(related_name='trades_users_requester', verbose_name='User Requisitante', to='gt.Users'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='trades',
            name='status_kind',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='trades_status', to='gt.Kind'),
=======
            field=models.ForeignKey(related_name='trades_status', verbose_name='Status da Troca', to='gt.Kind'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='trades',
            name='trade_kind',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='trades_kind', to='gt.Kind'),
=======
            field=models.ForeignKey(related_name='trades_kind', verbose_name='Tipo da Troca', to='gt.Kind'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='games',
            name='id_genre',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Genres'),
=======
            field=models.ForeignKey(verbose_name='Gênero', to='gt.Genres'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_game',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Games'),
=======
            field=models.ForeignKey(verbose_name='Jogo', to='gt.Games'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_user',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Users'),
=======
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='game_console',
            name='id_game',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Games'),
=======
            field=models.ForeignKey(verbose_name='Jogo', to='gt.Games'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='developers',
            name='dev_kind',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Kind'),
=======
            field=models.ForeignKey(verbose_name='Tipo', to='gt.Kind'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='consoles',
            name='id_dev',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Developers'),
=======
            field=models.ForeignKey(verbose_name='Desenvolvedor', to='gt.Developers'),
>>>>>>> origin/master
        ),
        migrations.AddField(
            model_name='chat',
            name='id_trade',
<<<<<<< HEAD
            field=models.ForeignKey(to='gt.Trades'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_user_requested',
            field=models.ForeignKey(related_name='chat_users_requested', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_user_requester',
            field=models.ForeignKey(related_name='chat_users_requester', to='gt.Users'),
=======
            field=models.ForeignKey(verbose_name='Troca', to='gt.Trades'),
>>>>>>> origin/master
        ),
    ]
