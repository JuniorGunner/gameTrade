from django.db import models
from django.contrib.auth.models import User

def upload_to_user(instance, filename):
    return 'images/users/%s/%s' % (instance.user.username, filename)

def upload_to_game(instance, filename):
    return 'images/games/%s/%s/%s' % (instance.id_console.name, instance.id_game.title, filename)

def upload_to_console(instance, filename):
    return 'images/consoles/%s/%s' % (instance.name, filename)

class Address(models.Model):
    street = models.CharField(max_length = 100)
    number = models.IntegerField()
    complement = models.CharField(max_length = 30)
    district = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 9)
    city = models.CharField(max_length = 50)
    uf = models.CharField(max_length = 2)
    country = models.CharField(max_length = 30)

class Users(models.Model):
    picture = models.ImageField(upload_to = upload_to_user, default = '') #REVISAR
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.OneToOneField(Address, on_delete = models.CASCADE)

    def __str__(self):
        return 'User: {}'.format(self.user.username)

class Kind(models.Model):
    group = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return 'Kind: {} - {}'.format(self.group, self.description)


class Developers(models.Model):
    description = models.CharField(max_length = 50)
    dev_kind = models.ForeignKey(Kind)

    def __str__(self) :
        return 'Dev.: {}'.format(self.description)

class Consoles(models.Model):
    id_dev = models.ForeignKey(Developers)
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    picture = models.ImageField(upload_to = upload_to_console, default = '') #REVISAR
    description = models.CharField(max_length = 300)

class Genres(models.Model):
    description = models.CharField(max_length = 100)

    def __str__(self):
        return 'Genre: {}'.format(self.description)

class Games(models.Model):
    id_dev = models.ForeignKey(Developers)
    id_genre = models.ForeignKey(Genres)
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    description = models.CharField(max_length = 300)

class Game_Console(models.Model):
    id_console = models.ForeignKey(Consoles)
    id_game = models.ForeignKey(Games)
    picture = models.ImageField(upload_to = upload_to_game, default = '') #REVISAR

class User_Game(models.Model):
    id_user = models.ForeignKey(Users)
    id_game_console = models.ForeignKey(Game_Console)
    rating = models.ForeignKey(Kind) #1 - Want, 2 - Have

    def __str__(self):
        return 'User_Game: {} - {} - {}'.format(self.id_user.user.username, self.id_game_console.id_game.title, self.rating.description)

class Game_Rating(models.Model):
    id_user = models.ForeignKey(Users)
    id_game = models.ForeignKey(Games)
    value = models.DecimalField(max_digits = 2, decimal_places = 2)

class Trades(models.Model):
    id_user_requester = models.ForeignKey(Users, related_name = 'trades_users_requester')
    id_user_requested = models.ForeignKey(Users, related_name = 'trades_user_requested')
    user_requester_status = models.BooleanField()
    user_requested_status = models.BooleanField()
    id_game_requester = models.ForeignKey(User_Game, blank = True, null = True, related_name = 'trades_games_requester')
    id_game_requested = models.ForeignKey(User_Game, blank = True, null = True, related_name = 'trades_games_requested')
    trade_kind = models.ForeignKey(Kind, related_name = 'trades_kind')
    status_kind = models.ForeignKey(Kind, related_name = 'trades_status')
    date = models.DateField(blank = True, null = True)

class Chat(models.Model):
    id_trade = models.ForeignKey(Trades)
    id_user_requester = models.ForeignKey(Users, related_name = 'chat_users_requester')
    id_user_requested = models.ForeignKey(Users, related_name = 'chat_users_requested')
    msg_started = models.TextField()
    msg_accepted = models.TextField()
    msg_finished = models.TextField()
    date_started = models.DateField()
    date_accepted = models.DateField()
    date_finished = models.DateField()

class User_Rating(models.Model):
    id_user = models.ForeignKey(Users)
    id_trade = models.ForeignKey(Trades)
    value = models.DecimalField(max_digits = 2, decimal_places = 2)
