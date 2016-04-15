from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="gt-home"),
	url(r'^login$', views.login, name="gt-login"),
	url(r'^register$', views.register, name="gt-register"),
	url(r'^my_account$', views.my_account, name="gt-my-account"),
	url(r'^game$', views.game, name="gt-game"),
	url(r'^games_by_console$', views.games_by_console, name="gt-games-by-console"),
	url(r'^user_account$', views.user_account, name="gt-user-account"),
	url(r'^search$', views.search, name="gt-search"),
    url(r'^about$', views.about, name="gt-about"),
]
