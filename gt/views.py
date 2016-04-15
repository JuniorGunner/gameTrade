from django.shortcuts import render

# Create your views here.
def home(request):
    active_page = 'home'
    return render(request, 'gt/home.html', {'active_page': active_page})

def login(request):
    active_page = 'login'
    return render(request, 'gt/login.html', {'active_page': active_page})

def register(request):
    active_page = 'register'
    return render(request, 'gt/user_register.html', {'active_page': active_page})

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
    active_page = 'about'
    return render(request, 'gt/about.html', {'active_page': active_page})

def error404(request):
    return render(request,'gt/404.html')
