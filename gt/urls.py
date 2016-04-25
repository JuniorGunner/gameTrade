from django.conf.urls import include, url
from django.contrib.auth.views import login as view_login, logout_then_login
from . import views

urlpatterns = [
    url(r'^$', views.home, name="gt-home"),
	url(r'^login/$', view_login, {'template_name': 'gt/check_login.html'}, name='gt-login'),
	url(r'^register/$', views.register, name="gt-register"),
	url(r'^my_account/$', views.my_account, name="gt-my-account"),
	url(r'^game/$', views.game, name="gt-game"),
	url(r'^games_by_console/(?P<console_id>\d+)/$', views.games_by_console, name="gt-games-by-console"),
	url(r'^user_accoun/t$', views.user_account, name="gt-user-account"),
	url(r'^search/$', views.search, name="gt-search"),
    url(r'^about/$', views.about, name="gt-about"),
    url(r'^logout/$', logout_then_login, {'login_url': '/login'}, name="gt-logout"),
]
