from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='sing in'),
    path('signup', views.signup, name='sign up'),
]