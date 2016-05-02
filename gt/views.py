from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import login as view_login

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gt.models import *

# Create your views here.
def lost_account(request):
    if 'user' in request.POST and 'email' in request.POST:
        try:
            user = User.objects.get(username = request.POST.get('user'), email = request.POST.get('email'))
            user_password = user.password
            email_subject = u"Recuperação de Senha - gameTrade"
            email_message = u"Link de redefinição de senha para %s : http://gametrade.pythonanywhere.com/ (função indisponível no momento)" % (user.username)
            user.email_user(subject = email_subject, message = email_message, from_email = 'gametrade016@gmail.com')
        except ObjectDoesNotExist:
            pass
    return redirect(view_login)

def home(request):
    return render(request, 'gt/home.html', {})

def register(request):
    if request.user.is_authenticated():
        return redirect('gt.views.my_account')
    else:
        return render(request, 'gt/user_register.html', {})

@login_required
def my_account(request):
    user_req = Users.objects.get(user = request.user)

    #removendo jogo da lista
    if 'game' in request.GET:
        User_Game.objects.get(pk = request.GET.get('game')).delete()

    games_have = User_Game.objects.filter(id_user = user_req, rating__description = 'Have')
    games_want = User_Game.objects.filter(id_user = user_req, rating__description = 'Want')

    return render(request, 'gt/my_account.html', {'user_req': user_req, 'games_have': games_have, 'games_want': games_want})

def game(request, console_id, game_id):
    game = get_object_or_404(Game_Console, id_game = game_id, id_console = console_id)

    req = 0
    if 'type' in request.GET and request.user.is_authenticated():
        req = request.GET['type']
        has_one = User_Game.objects.filter(id_game_console = game, id_user__user = request.user)
        if len(has_one) == 0:
            if req == 'want':
                req = Kind.objects.get(description = 'Want')
            elif req == 'have':
                req = Kind.objects.get(description = 'Have')
            user_new = Users.objects.get(user = request.user)
            ug = User_Game(id_user = user_new, id_game_console = game, rating = req)
            ug.save()

    users_have = User_Game.objects.filter(id_game_console = game, rating__description = 'Have')
    users_want = User_Game.objects.filter(id_game_console = game, rating__description = 'Want')
    other_consoles = Game_Console.objects.filter(id_game = game_id)
    rating = Game_Rating.objects.filter(id_game = game.id_game).aggregate(Avg('value'))
    user_want = 0
    user_have = 0
    if request.user.is_authenticated():
        user = Users.objects.get(user = request.user)
        try:
            user_have = users_have.get(id_user = user)
        except ObjectDoesNotExist:
            user_have = None
        try:
            user_want = users_want.get(id_user = user)
        except ObjectDoesNotExist:
            user_want = None
    return render(request, 'gt/game.html', {'game': game, 'users_have': users_have, 'users_want': users_want, \
    'other_consoles': other_consoles, 'rating': rating, 'user_have': user_have, 'user_want': user_want, 'req': req})

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

def user_account(request, user_id):
    user = get_object_or_404(Users, pk = user_id)

    games_have = User_Game.objects.filter(id_user = user, rating__description = 'Have')
    games_want = User_Game.objects.filter(id_user = user, rating__description = 'Want')

    #inicio bloco de troca
    #user_requester = None
    #user_requested = None

    if 'game' in request.GET and 'type' in request.GET and request.user.is_authenticated():
        user_requested = user
        user_requester = Users.objects.get(user = request.user)
        game = Game_Console.objects.get(pk = request.GET.get('game'))

        req_type = request.GET.get('type')
        #if req_type == 'have':
        #elif req_type == 'want':
        #elif req_type == 'donate':
    #fim bloco de troca

    requester_games_have = 0
    requester_games_want = 0
    if request.user.is_authenticated():
        requester_games_want = Game_Console.objects.filter(user_game__id_user__user = request.user, user_game__rating__description = 'Want')
        requester_games_have = Game_Console.objects.filter(user_game__id_user__user = request.user, user_game__rating__description = 'Have')

    rating = User_Rating.objects.filter(id_user = user).aggregate(Avg('value'))
    rating_count = User_Rating.objects.filter(id_user = user).count()

    return render(request, 'gt/user_account.html', {'user_page': user, 'games_have': games_have, 'games_want': games_want, 'rating': rating \
    , 'rating_count': rating_count, 'requester_games_have': requester_games_have, 'requester_games_want': requester_games_want})

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
