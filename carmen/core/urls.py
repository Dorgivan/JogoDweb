from django.urls import path

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path('',auth_views.login, {'template_name': 'index.html'},name='index-login'),
    path('cadastro/',views.CadastroUser.as_view(),name='cadastro'),
    path('cadastro/dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('cadastro/logout/',auth_views.logout, {'template_name': 'conta/back.html'}, name='logout'),
    path('cadastro/dashboard/jogo/<pk>/',views.Game.as_view(), name='jogo'),
]
