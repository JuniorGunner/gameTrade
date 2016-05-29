from django.contrib import admin
from gt.models import *

# Register your models here.
class KindAdmin(admin.ModelAdmin):
    model = Kind
    list_display = ['group', 'description']
admin.site.register(Kind, KindAdmin)

class DevAdmin(admin.ModelAdmin):
    model = Developers
    list_display = ['description']
admin.site.register(Developers, DevAdmin)

class GamesAdmin(admin.ModelAdmin):
    model = Games
    list_display = ['title', 'year', 'description']
admin.site.register(Games, GamesAdmin)

class ConsolesAdmin(admin.ModelAdmin):
    model = Consoles
    list_display = ['name', 'year', 'picture', 'description']
admin.site.register(Consoles, ConsolesAdmin)

class GenresAdmin(admin.ModelAdmin):
    model = Genres
    list_display = ['description']
admin.site.register(Genres, GenresAdmin)

admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Game_Console)
admin.site.register(User_Game)
admin.site.register(Game_Rating)
admin.site.register(Trades)
