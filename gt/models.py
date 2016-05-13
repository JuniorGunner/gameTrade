from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings

def upload_to_user(instance, filename):
    return 'images/users/%s/%s' % (instance.user.username, filename)

def upload_to_game(instance, filename):
    return 'images/games/%s/%s/%s' % (instance.id_console.name, instance.id_game.title, filename)

def upload_to_console(instance, filename):
    return 'images/consoles/%s/%s' % (instance.name, filename)

class Address(models.Model):
    street = models.CharField('Rua', max_length = 200, blank = True)
    number = models.IntegerField('Nº', blank = True)
    complement = models.CharField('Complemento', max_length = 30, blank = True)
    district = models.CharField('Bairro', max_length = 50, blank = True)
    zip_code = models.CharField('CEP', max_length = 9, blank = True)
    city = models.CharField('Cidade', max_length = 50, blank = True)
    uf = models.CharField('UF', max_length = 2, blank = True)
    country = models.CharField('País', max_length = 30, blank = True)

    def __str__(self):
        return 'Address: {}, {} - {} - {} - {}'.format(self.street, self.number, self.district, self.city, self.uf)

class Users(models.Model):
    picture = models.ImageField('Imagem', upload_to = upload_to_user, default = '/static/images/UserDefault.png', blank = True, null = True) #REVISAR
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuário')
    address = models.OneToOneField(Address, on_delete = models.CASCADE, verbose_name = 'Endereço')

    def __str__(self):
        return 'User: {}'.format(self.user.username)

class Kind(models.Model):
    group = models.CharField('Grupo', max_length = 100)
    description = models.CharField('Descrição', max_length = 200)

    def __str__(self):
        return 'Tipo: {} - {}'.format(self.group, self.description)


class Developers(models.Model):
    name = models.CharField('Nome', max_length = 100, blank = True)
    dev_kind = models.ForeignKey(Kind, verbose_name = 'Tipo')

    def __str__(self) :
        return 'Dev.: {}'.format(self.name)

class Consoles(models.Model):
    id_dev = models.ForeignKey(Developers, verbose_name = 'Desenvolvedor')
    name = models.CharField('Nome', max_length = 100)
    year = models.IntegerField('Ano', blank = True, null = True)
    picture = models.ImageField('Imagem', upload_to = upload_to_console, default = '', blank = True, null = True) #REVISAR
    description = models.TextField('Descrição', blank = True)

    def __str__(self):
        return 'Console: {}'.format(self.name)

class Genres(models.Model):
    description = models.CharField(max_length = 100)

    def __str__(self):
        return 'Genre: {}'.format(self.description)

class Games(models.Model):
    id_dev = models.ForeignKey(Developers, verbose_name = 'Desenvolvedor')
    id_genre = models.ForeignKey(Genres, verbose_name = 'Gênero')
    title = models.CharField('Título', max_length = 100)
    year = models.IntegerField('Ano', blank = True, null = True)
    description = models.TextField('Descrição', max_length = 300, blank = True)

    def __str__(self):
        return 'Game: {}'.format(self.title)

class Game_Console(models.Model):
    id_console = models.ForeignKey(Consoles, verbose_name = 'Console')
    id_game = models.ForeignKey(Games, verbose_name = 'Jogo')
    picture = models.ImageField('Imagem', upload_to = upload_to_game, default = '', blank = True, null = True) #REVISAR

    def __str__(self):
        return 'gameConsole: {} - {}'.format(self.id_console.name, self.id_game.title)

class User_Game(models.Model):
    id_user = models.ForeignKey(Users, verbose_name = 'Usuário')
    id_game_console = models.ForeignKey(Game_Console, verbose_name = 'Jogo/Console')
    want_have = models.ForeignKey(Kind, verbose_name = 'Quero/Tenho') #1 - Want, 2 - Have

class Game_Rating(models.Model):
    id_user = models.ForeignKey(Users, verbose_name = 'Usuário')
    id_game = models.ForeignKey(Games, verbose_name = 'Jogo')
    value = models.DecimalField('Avaliação do Jogo', max_digits = 4, decimal_places = 2)

class Trades(models.Model):
    id_user_requester = models.ForeignKey(Users, verbose_name = 'User Requisitante', related_name = 'trades_users_requester')
    id_user_requested = models.ForeignKey(Users, verbose_name = 'User Requisitado', related_name = 'trades_user_requested')
    user_requester_status = models.BooleanField('Status Requisitante')
    user_requested_status = models.BooleanField('Status Requisitado')
    id_game_requester = models.ForeignKey(Games, verbose_name = 'Jogo Requisitante', related_name = 'trades_games_requester')
    id_game_requested = models.ForeignKey(Games, verbose_name = 'Jogo Requisitado', related_name = 'trades_games_requested')
    trade_kind = models.ForeignKey(Kind, verbose_name = 'Tipo da Troca', related_name = 'trades_kind')
    status_kind = models.ForeignKey(Kind, verbose_name = 'Status da Troca', related_name = 'trades_status')
    date = models.DateField('Data da Troca', auto_now_add = True)

class Chat(models.Model):
    id_trade = models.ForeignKey(Trades, verbose_name = 'Troca')
    msg_started = models.TextField('Mensagem Inicial', blank = True)
    msg_accepted = models.TextField('Mensagem de Aceitação', blank = True)
    msg_finished = models.TextField('Mensagem de Conclusão', blank = True)
    date_started = models.DateField('Data Primeira Mensagem', auto_now_add = True, blank = True, null = True)
    date_updated = models.DateField('Data de Atualização', auto_now = True, blank = True, null = True)
    date_finished = models.DateField('Data de Conclusão', blank = True, null = True)

class User_Rating(models.Model):
    id_user = models.ForeignKey(Users, verbose_name = 'Usuário')
    id_trade = models.ForeignKey(Trades, verbose_name = 'Troca')
    value = models.DecimalField('Avaliação do Usuário', max_digits = 4, decimal_places = 2)
