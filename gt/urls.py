from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
	url(r'^home$', views.home),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^my_account$', views.my_account),
	url(r'^game$', views.game),
	url(r'^games_by_console$', views.games_by_console),
	url(r'^user_account$', views.user_account),
	url(r'^search$', views.search),
]
