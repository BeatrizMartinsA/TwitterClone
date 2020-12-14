from core import views
from django.urls import path

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),
    path('api/list_tweets', views.list_tweets),
    path('api/follow', views.follow),
    path('api/unfollow', views.unfollow),
    path('api/tweet', views.tweet),
    path('api/get_user_details', views.get_user_details),
    path('api/signup', views.signup),
]
