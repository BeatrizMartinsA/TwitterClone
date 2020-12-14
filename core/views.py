# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, globalsettings_svc, tweeter_svc, user_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def signup(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    user_svc.create_user(username, first_name, last_name, email, password)
    return JsonResponse({})

    # def tweet(request):
    # text = request.POST['text']
    # tweet = tweeter_svc.tweet(request.user, text)
    # return JsonResponse(tweet)



# def signup(request):
#     user_dic = json.loads(request.POST.get('user', '{}'))
#     try:
#         user = auth_svc.signup(user_dic)
#         auth.login(request, user, backend=AUTH_BACKEND)
#         user_dic_res = _user2dict(user)
#         return JsonResponse(user_dic_res)
#     except ValidationError as ex:
#         dict_response = {'error': error_str(ex)}
#         existing_user = ex.args[1]
#         if existing_user and getattr(existing_user, 'id', False):
#             dict_response.update({
#                 'id': existing_user.id,
#                 'name': existing_user.get_full_name(),
#                 'photo_url': existing_user.profile.photo_url,
#                 'email': existing_user.email if existing_user.email == user_dic['email'] else None,
#                 'cell_phone': existing_user.profile.cell_phone if existing_user.profile.cell_phone == user_dic[
#                     'phone'] else None,
#                 'has_password': existing_user.has_usable_password(),
#                 'has_facebook': existing_user.social_auth.filter(provider='facebook').exists(),
#                 'is_active': existing_user.is_active
#             })
# #         return JsonResponse(dict_response)

#         def create_user_from_dict(user_dic):
#     validate_user_dic(user_dic)
#     name, password = [user_dic.get(k) for k in ('name', 'password')]
#     email = user_dic['email'].lower().strip()
#     namesplit = name.split()
#     user = create_user(
#         username=email,
#         email=email,
#         first_name=namesplit[0],
#         last_name=' '.join(namesplit[1:]),
#         password=password or random_code(16),
#         phone=only_numbers(user_dic['phone']),
#     )
#     return user



def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)


def list_tweets(request):
    loggeduser = request.user if request.user.is_authenticated else None
    username = request.GET.get('username')
    tweets = tweeter_svc.list_tweets(loggeduser, username)
    return JsonResponse({'tweets': tweets})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d


@ajax_login_required
def follow(request):
    username = request.POST['username']
    tweeter_svc.follow(request.user, username)
    return JsonResponse({})


@ajax_login_required
def unfollow(request):
    username = request.POST['username']
    tweeter_svc.unfollow(request.user, username)
    return JsonResponse({})


@ajax_login_required
def tweet(request):
    text = request.POST['text']
    tweet = tweeter_svc.tweet(request.user, text)
    return JsonResponse(tweet)


def get_user_details(request):
    loggeduser = request.user if request.user.is_authenticated else None
    username = request.GET.get('username')
    userdetails = user_svc.get_details(loggeduser, username)
    return JsonResponse(userdetails)
