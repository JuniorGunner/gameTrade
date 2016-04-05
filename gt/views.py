from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'gt/home.html', {})
	
def login(request):
	return render(request, 'gt/login.html', {})

def register(request):
	return render(request, 'gt/user_register.html', {})

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
