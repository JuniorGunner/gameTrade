from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from gt.forms import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gt.models import *

# Create your views here.
def home(request):
    return render(request, 'gt/home.html', {})

def register(request):
    if request.user.is_authenticated():
        return redirect('gt.views.my_account')
    else:
        formAddress = AddressForm()
        formUser = RegisterForm()
        if request.method == 'POST':
            formAddress = AddressForm(request.POST, prefix = 'addressForm')
            formUser = RegisterForm(request.POST, prefix = 'userForm')
            if formUser.is_valid() and formAddress.is_valid():
                a = formAddress.save()
                u = formUser.save()
                n = Users.objects.create(address = Address.objects.latest('id'), user = User.objects.latest('id'))
                n.save()
                return redirect('gt.views.my_account')
        context = {
            'formUser': formUser,
            'formAddress': formAddress
        }
        return render(request, 'gt/user_register.html', context)

@login_required
def my_account(request):
    users = Users.objects.get(user = request.user)
    return render(request, 'gt/my_account.html', {'users': users})

def game(request, console_id, game_id):
    game = get_object_or_404(Game_Console, id_game = game_id, id_console = console_id)
    users_have = User_Game.objects.filter(id_game_console = game, rating__description = 'Have')
    users_want = User_Game.objects.filter(id_game_console = game, rating__description = 'Want')
    other_consoles = Game_Console.objects.filter(id_game = game_id)
    return render(request, 'gt/game.html', {'game': game, 'users_have': users_have, 'users_want': users_want, 'other_consoles': other_consoles})

def games_by_console(request, console_id):
    console = get_object_or_404(Consoles, pk = console_id)
    games = Game_Console.objects.filter(id_console = console).order_by('id_game__title')
    paginator = Paginator(games, 10)
    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
        page = 1
    except EmptyPage:
        games = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    page = int(page)
    init = 1
    if paginator.num_pages > 4:
        final = 6
    else:
        final = paginator.num_pages + 1
    if page > 3 and paginator.num_pages > 5:
        if page <= paginator.num_pages - 2:
            init = page - 2
            final = page + 3
        else:
            final = paginator.num_pages + 1
            init = final - 5
    return render(request, 'gt/games_by_console.html', {'console': console, 'games': games, 'n': range(init, final), 'page': page})

def user_account(request):
	return render(request, 'gt/user_account.html', {})

def search(request):
        keyword = request.GET['search-value']
        result = 0
        if len(keyword) == 0:
            keyword = -1
            message = u'Utilize a caixa de pesquisa para buscar por jogo ou usuário'
            return render(request, 'gt/search.html', {'keyword': keyword, 'message': message})
        elif request.GET['search'] == 'game':
            result = Game_Console.objects.filter(id_game__title__icontains = keyword).order_by('id_game__title')
        else:
            result = Users.objects.filter(user__username__icontains = keyword, user__is_superuser = 0).order_by('user__username')
        result_length = len(result)
        if result_length == 0:
            message = u'Nenhum registro encontrado'
            return render(request, 'gt/search.html', {'keyword': keyword, 'message': message})
        else:
            message = u'%d registro(s) encontrado(s). Palavra-chave: %s' % (result_length, keyword)
            paginator = Paginator(result, 10)
            page = request.GET.get('page')
            try:
                result = paginator.page(page)
            except PageNotAnInteger:
                result = paginator.page(1)
                page = 1
            except EmptyPage:
                result = paginator.page(paginator.num_pages)
                page = paginator.num_pages
            page = int(page)
            init = 1
            if paginator.num_pages > 4:
                final = 6
            else:
                final = paginator.num_pages + 1
            if page > 3 and paginator.num_pages > 5:
                if page <= paginator.num_pages - 2:
                    init = page - 2
                    final = page + 3
                else:
                    final = paginator.num_pages + 1
                    init = final - 5
            return render(request, 'gt/search.html', {'keyword': keyword, 'message': message, 'result': result, 'n': range(init, final), 'search': request.GET['search'], 'page': page})


def about(request):
    return render(request, 'gt/about.html', {})

def error404(request):
    return render(request,'gt/404.html')
