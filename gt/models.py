from django.db import models
from django.contrib.auth.models import User

def upload_to_user(instance, filename):
    return 'images/%s/%s' % (instance.user.username, filename)

def upload_to_game(instance, filename):
    return 'images/%s/%s' % (instance.games.id, filename)

def upload_to_console(instance, filename):
    return 'images/%s/%s' % (instance.consoles.id, filename)

class Users(models.Model):
    picture = models.ImageField(upload_to = upload_to_user, default = '') #REVISAR
    user = models.OneToOneField(User, on_delete = models.CASCADE)


class Address(models.Model):
    id_user = models.ForeignKey(Users)
    street = models.CharField(max_length = 100)
    number = models.IntegerField()
    complement = models.CharField(max_length = 30)
    district = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 9)
    city = models.CharField(max_length = 50)
    uf = models.CharField(max_length = 2)
    country = models.CharField(max_length = 30)

class Developers(models.Model):
    description = models.CharField(max_length = 50)
    kind = models.IntegerField() #1 - Consoles, 2 - Games, 3 - Both

class Consoles(models.Model):
    id_dev = models.ForeignKey(Developers)
    name = models.CharField(max_length = 100)
    year = models.IntegerField()
    picture = models.ImageField(upload_to = upload_to_console, default = '') #REVISAR
    description = models.CharField(max_length = 300)

class Genres(models.Model):
    description = models.CharField(max_length = 100)

class Games(models.Model):
    id_dev = models.ForeignKey(Developers)
    id_genre = models.ForeignKey(Genres)
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    picture = models.ImageField(upload_to = upload_to_game, default = '') #REVISAR
    description = models.CharField(max_length = 300)

class Game_Console(models.Model):
    id_console = models.ForeignKey(Consoles)
    id_game = models.ForeignKey(Games)

class User_Game(models.Model):
    id_user = models.ForeignKey(Users)
    id_game = models.ForeignKey(Games)
    rating = models.IntegerField() #1 - Want, 2 - Have

class Game_Rating(models.Model):
    id_user = models.ForeignKey(Users)
    id_game = models.ForeignKey(Games)
    value = models.DecimalField(max_digits = 2, decimal_places = 2)

class Trade_Kind(models.Model):
    description = models.CharField(max_length = 100)

class Status(models.Model):
    description = models.CharField(max_length = 100)

class Trades(models.Model):
    id_user_requester = models.ForeignKey(Users, related_name = 'trades_users_requester')
    id_user_requested = models.ForeignKey(Users, related_name = 'trades_user_requested')
    user_requester_status = models.BooleanField()
    user_requested_status = models.BooleanField()
    id_game_requester = models.ForeignKey(Games, related_name = 'trades_games_requester')
    id_game_requested = models.ForeignKey(Games, related_name = 'trades_games_requested')
    id_trade_kind = models.ForeignKey(Trade_Kind)
    id_status = models.ForeignKey(Status)
    date = models.DateField()

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
