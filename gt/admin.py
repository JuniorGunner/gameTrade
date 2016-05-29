from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from gt.models import *
#from gt.forms import *

# Register your models here.
class KindAdmin(admin.ModelAdmin):
    model = Kind
    list_display = ['group', 'description']

admin.site.register(Kind, KindAdmin)

class DevAdmin(admin.ModelAdmin):
    model = Developers
    list_display = ['name']

admin.site.register(Developers, DevAdmin)

class GamesAdmin(admin.ModelAdmin):
    model = Games
    list_display = ['title', 'year', 'description']
    search_fields = ['title', 'year']

admin.site.register(Games, GamesAdmin)

class ConsolesAdmin(admin.ModelAdmin):
    model = Consoles
    list_display = ['name', 'year', 'picture', 'description']
    search_fields = ['name', 'year']

admin.site.register(Consoles, ConsolesAdmin)

class GenresAdmin(admin.ModelAdmin):
    model = Genres
    list_display = ['description']
    search_fields = ['description']

admin.site.register(Genres, GenresAdmin)

admin.site.register(Users)

class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ['street', 'number', 'complement', 'district', 'zip_code', 'city', 'uf', 'country']
admin.site.register(Address)

admin.site.register(Game_Console)
admin.site.register(User_Game)
admin.site.register(Game_Rating)
admin.site.register(Trades)
