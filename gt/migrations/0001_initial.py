# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import gt.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('street', models.CharField(blank=True, verbose_name='Rua', max_length=200)),
                ('number', models.IntegerField(blank=True, verbose_name='Nº')),
                ('complement', models.CharField(blank=True, verbose_name='Complemento', max_length=30)),
                ('district', models.CharField(blank=True, verbose_name='Bairro', max_length=50)),
                ('zip_code', models.CharField(blank=True, verbose_name='CEP', max_length=9)),
                ('city', models.CharField(blank=True, verbose_name='Cidade', max_length=50)),
                ('uf', models.CharField(blank=True, verbose_name='UF', max_length=2)),
                ('country', models.CharField(blank=True, verbose_name='País', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('msg_started', models.TextField(blank=True, verbose_name='Mensagem Inicial')),
                ('msg_accepted', models.TextField(blank=True, verbose_name='Mensagem de Aceitação')),
                ('msg_finished', models.TextField(blank=True, verbose_name='Mensagem de Conclusão')),
                ('date_started', models.DateField(auto_now_add=True, null=True, verbose_name='Data Primeira Mensagem')),
                ('date_updated', models.DateField(auto_now=True, null=True, verbose_name='Data de Atualização')),
                ('date_finished', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Consoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Ano')),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_console)),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, verbose_name='Nome', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game_Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_game)),
                ('id_console', models.ForeignKey(verbose_name='Console', to='gt.Consoles')),
            ],
        ),
        migrations.CreateModel(
            name='Game_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.DecimalField(max_digits=4, verbose_name='Avaliação do Jogo', decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Ano')),
                ('description', models.TextField(blank=True, verbose_name='Descrição', max_length=300)),
                ('id_dev', models.ForeignKey(verbose_name='Desenvolvedor', to='gt.Developers')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('group', models.CharField(verbose_name='Grupo', max_length=100)),
                ('description', models.CharField(verbose_name='Descrição', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_requester_status', models.BooleanField(verbose_name='Status Requisitante')),
                ('user_requested_status', models.BooleanField(verbose_name='Status Requisitado')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data da Troca')),
                ('id_game_requested', models.ForeignKey(related_name='trades_games_requested', verbose_name='Jogo Requisitado', to='gt.Games')),
                ('id_game_requester', models.ForeignKey(related_name='trades_games_requester', verbose_name='Jogo Requisitante', to='gt.Games')),
            ],
        ),
        migrations.CreateModel(
            name='User_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('id_game_console', models.ForeignKey(verbose_name='Jogo/Console', to='gt.Game_Console')),
            ],
        ),
        migrations.CreateModel(
            name='User_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.DecimalField(max_digits=4, verbose_name='Avaliação do Usuário', decimal_places=2)),
                ('id_trade', models.ForeignKey(verbose_name='Troca', to='gt.Trades')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(default='', blank=True, null=True, verbose_name='Imagem', upload_to=gt.models.upload_to_user)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254)),
                ('address', models.OneToOneField(verbose_name='Endereço', to='gt.Address')),
                ('user', models.OneToOneField(verbose_name='Usuário', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user_rating',
            name='id_user',
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='user_game',
            name='id_user',
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='user_game',
            name='want_have',
            field=models.ForeignKey(verbose_name='Quero/Tenho', to='gt.Kind'),
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requested',
            field=models.ForeignKey(related_name='trades_user_requested', verbose_name='User Requisitado', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='trades',
            name='id_user_requester',
            field=models.ForeignKey(related_name='trades_users_requester', verbose_name='User Requisitante', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='trades',
            name='status_kind',
            field=models.ForeignKey(related_name='trades_status', verbose_name='Status da Troca', to='gt.Kind'),
        ),
        migrations.AddField(
            model_name='trades',
            name='trade_kind',
            field=models.ForeignKey(related_name='trades_kind', verbose_name='Tipo da Troca', to='gt.Kind'),
        ),
        migrations.AddField(
            model_name='games',
            name='id_genre',
            field=models.ForeignKey(verbose_name='Gênero', to='gt.Genres'),
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_game',
            field=models.ForeignKey(verbose_name='Jogo', to='gt.Games'),
        ),
        migrations.AddField(
            model_name='game_rating',
            name='id_user',
            field=models.ForeignKey(verbose_name='Usuário', to='gt.Users'),
        ),
        migrations.AddField(
            model_name='game_console',
            name='id_game',
            field=models.ForeignKey(verbose_name='Jogo', to='gt.Games'),
        ),
        migrations.AddField(
            model_name='developers',
            name='dev_kind',
            field=models.ForeignKey(verbose_name='Tipo', to='gt.Kind'),
        ),
        migrations.AddField(
            model_name='consoles',
            name='id_dev',
            field=models.ForeignKey(verbose_name='Desenvolvedor', to='gt.Developers'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_trade',
            field=models.ForeignKey(verbose_name='Troca', to='gt.Trades'),
        ),
    ]
