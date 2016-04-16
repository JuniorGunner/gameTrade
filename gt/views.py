from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'gt/home.html', {})

"""def login(request):
    if request.method == 'POST':

        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                active_page = 'home'
                return render(request, reverse('gt-home'),{'active_page': active_page})
            else:
                active_page = 'login'
                msg = 'Conta desativada'
                return render(request, 'gt/login.html',{'active_page': active_page, 'msg': msg})
        else:
            active_page = 'login'
            msg = 'Usuário ou Senha Inválido'
            return render(request, 'gt/login.html',{'active_page': active_page, 'msg': msg})
    else:
        active_page = 'login'
        return render(request, 'gt/login.html',{'active_page': active_page})"""

def register(request):
    if request.user.is_authenticated():
        return render(request, 'gt/my_account.html', {'page_url':'my_account'})
    else:
        return render(request, 'gt/user_register.html', {})

@login_required
def my_account(request):
	return render(request, 'gt/my_account.html', {})

def game(request):
	return render(request, 'gt/game.html', {})

def games_by_console(request):
	return render(request, 'gt/games_by_console.html', {})

def user_account(request):
	return render(request, 'gt/user_account.html', {})

def search(request):
	return render(request, 'gt/search.html', {})

def about(request):
    return render(request, 'gt/about.html', {})

def error404(request):
    return render(request,'gt/404.html')
