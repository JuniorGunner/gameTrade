from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import login as view_login
from itertools import chain
import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gt.models import *

# Create your views here.
def lost_account(request):
    if 'user' in request.POST and 'email' in request.POST:
        try:
            user = User.objects.get(username = request.POST.get('user'),
                email = request.POST.get('email'))
            user_password = user.password
            email_subject = u"Recuperação de Senha - gameTrade"
            email_message = u"Link de redefinição de senha para %s : " + \
            u"http://gametrade.pythonanywhere.com/ (função indisponível no " + \
            u"momento)" % (user.username)
            user.email_user(subject = email_subject, message = email_message,
            from_email = 'gametrade016@gmail.com')
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

    #abas tenho e quero
    games_have = User_Game.objects.filter(id_user = user_req,
    rating__description = 'Have')
    games_want = User_Game.objects.filter(id_user = user_req,
    rating__description = 'Want')

    pending_requester = Trades.objects.filter(id_user_requester = user_req,
    status_kind__description = 'Pending').values_list('id_game_requester',
    flat = True)
    pending_requested = Trades.objects.filter(id_user_requested = user_req,
    status_kind__description = 'Pending').values_list('id_game_requested',
    flat = True)
    requested = Trades.objects.filter(
    id_user_requester = user_req,
    status_kind__description = 'Requested').values_list('id_game_requester',
    flat = True)

    user_trades = list(chain(pending_requester, pending_requested, requested))

    games_want = games_want.exclude(id__in = user_trades)

    return render(request, 'gt/my_account.html', {
    'user_req': user_req,
    'games_have': games_have,
    'games_want': games_want})

def game(request, console_id, game_id):
    game = get_object_or_404(Game_Console, id_game = game_id,
    id_console = console_id)

    req = 0
    if 'type' in request.POST and request.user.is_authenticated():
        req = request.POST['type']
        has_one = User_Game.objects.filter(id_game_console = game,
        id_user__user = request.user)
        if len(has_one) == 0:
            if req == 'want':
                req = Kind.objects.get(description = 'Want')
            elif req == 'have':
                req = Kind.objects.get(description = 'Have')
            user_new = Users.objects.get(user = request.user)
            ug = User_Game(id_user = user_new, id_game_console = game,
            rating = req)
            ug.save()

    users_have = User_Game.objects.filter(id_game_console = game,
    rating__description = 'Have')
    users_want = User_Game.objects.filter(id_game_console = game,
    rating__description = 'Want')

    user_want = None
    user_have = None

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

    pending_requester = Trades.objects.filter(
    id_game_requester__id_game_console = game,
    status_kind__description = 'Pending').values_list('id_user_requester',
    flat = True)
    pending_requested = Trades.objects.filter(
    id_game_requested__id_game_console = game,
    status_kind__description = 'Pending').values_list('id_user_requested',
    flat = True)

    game_trades = list(chain(pending_requester, pending_requested))

    users_have = users_have.exclude(id_user__in = game_trades)

    other_consoles = Game_Console.objects.filter(id_game = game_id)
    rating = Game_Rating.objects.filter(id_game = game.id_game).aggregate(
    Avg('value'))

    return render(request, 'gt/game.html', {
    'game': game,
    'users_have': users_have,
    'users_want': users_want,
    'other_consoles': other_consoles,
    'rating': rating,
    'user_have': user_have,
    'user_want': user_want,
    'req': req,
    'game_trades': game_trades})

def games_by_console(request, console_id):
    console = get_object_or_404(Consoles, pk = console_id)
    games = Game_Console.objects.filter(id_console = console).order_by(
    'id_game__title')
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
    return render(request, 'gt/games_by_console.html', {
        'console': console,
        'games': games,
        'n': range(init, final),
        'page': page})

def user_account(request, user_id):
    user = get_object_or_404(Users, pk = user_id)

    #inicio bloco de troca
    has_trade_requester = False
    has_trade_requested = False

    if request.user.is_authenticated:

        user_requester = None
        user_requested = None

        has_trade_requester = Trades.objects.filter(
            id_user_requested = user,
            id_user_requester__user = request.user,
            status_kind__description = 'Requested').exists()
        has_trade_requested = Trades.objects.filter(
            id_user_requested__user = request.user,
            id_user_requester = user,
            status_kind__description = 'Requested').exists()

        if 'game' in request.POST and 'type' in request.POST:
            if not has_trade_requester and not has_trade_requested:
                user_requested = user
                user_requester = Users.objects.get(user = request.user)
                game = User_Game.objects.get(id_user = user_requested,
                    id_game_console = request.POST.get('game'))
                status = Kind.objects.get(description = 'Requested')
                req_type = request.POST.get('type')

                if req_type == 'have':
                    req_type = Kind.objects.get(description = 'Trade')
                    trade = Trades(
                        id_user_requester = user_requester,
                        id_user_requested = user_requested,
                        user_requester_status = True,
                        user_requested_status = False,
                        id_game_requested = game,
                        trade_kind = req_type,
                        status_kind = status
                    )
                elif req_type == 'donate':
                    req_type = Kind.objects.get(description = 'Donate')
                    trade = Trades(
                        id_user_requester = user_requester,
                        id_user_requested = user_requested,
                        user_requester_status = True,
                        user_requested_status = False,
                        id_game_requester = game,
                        trade_kind = req_type,
                        status_kind = status
                    )
                trade.save()
                has_trade_requester = True
                has_trade_requested = False
            elif not has_trade_requester and has_trade_requested:
                user_requested = Users.objects.get(user = request.user)
                user_requester = user
                game = User_Game.objects.get(id_user = user_requester,
                    id_game_console = request.POST.get('game'))
                status = Kind.objects.get(description = 'Pending')
                trade = Trades.objects.get(
                    id_user_requested__user = request.user,
                    id_user_requester = user,
                    status_kind__description = 'Requested')
                trade.id_game_requester = game
                trade.date = datetime.date.today()
                trade.status_kind = status
                trade.user_requested_status = False
                trade.user_requester_status = False
                trade.save()
                User_Game.objects.get(
                    id_game_console = trade.id_game_requester.id_game_console,
                    id_user = user_requested,
                    rating__description = 'Want').delete()
                User_Game.objects.get(
                    id_game_console = trade.id_game_requested.id_game_console,
                    id_user = user_requester,
                    rating__description = 'Want').delete()
                has_trade_requester = False
                has_trade_requested = False
    #fim bloco de troca

    requester_games_have = 0
    requester_games_want = 0

    if request.user.is_authenticated() and (has_trade_requested or \
    not has_trade_requester):
        requester_games_want = Game_Console.objects.filter(
            user_game__id_user__user = request.user,
            user_game__rating__description = 'Want')
        requester_games_have = Game_Console.objects.filter(
            user_game__id_user__user = request.user,
            user_game__rating__description = 'Have')

    rating = User_Rating.objects.filter(id_user = user).aggregate(Avg('value'))
    rating_count = User_Rating.objects.filter(id_user = user).count()

    games_have = User_Game.objects.filter(id_user = user,
    rating__description = 'Have')
    games_want = User_Game.objects.filter(id_user = user,
    rating__description = 'Want')

    pending_requester = Trades.objects.filter(
        id_user_requester = user,
        status_kind__description = 'Pending').values_list(
        'id_game_requester',
        flat = True)
    pending_requested = Trades.objects.filter(
        id_user_requested = user,
        status_kind__description = 'Pending').values_list(
        'id_game_requested',
        flat = True)

    user_trades = list(chain(pending_requester, pending_requested))

    games_have = games_have.exclude(id__in = user_trades)

    return render(request, 'gt/user_account.html', {
    'user_page': user,
    'games_have': games_have,
    'games_want': games_want,
    'rating': rating,
    'rating_count': rating_count,
    'requester_games_have': requester_games_have,
    'requester_games_want': requester_games_want
    })

def search(request):
        keyword = request.GET['search-value']
        result = 0
        if len(keyword) == 0:
            keyword = -1
            message = \
            u'Utilize a caixa de pesquisa para buscar por jogo ou usuário'
            return render(request, 'gt/search.html', {
                'keyword': keyword,
                'message': message})
        elif request.GET['search'] == 'game':
            result = Game_Console.objects.filter(
            id_game__title__icontains = keyword).order_by('id_game__title')
        else:
            result = Users.objects.filter(
            user__username__icontains = keyword,
            user__is_superuser = 0).order_by('user__username')
        result_length = len(result)
        if result_length == 0:
            message = u'Nenhum registro encontrado'
            return render(request, 'gt/search.html', {'keyword': keyword,
            'message': message})
        else:
            message = u'%d registro(s) encontrado(s). Palavra-chave: %s' % \
            (result_length, keyword)
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
            return render(request, 'gt/search.html', {
            'keyword': keyword,
            'message': message,
            'result': result,
            'n': range(init, final),
            'search': request.GET['search'],
            'page': page})


def about(request):
    return render(request, 'gt/about.html', {})

def error404(request):
    return render(request,'gt/404.html')
