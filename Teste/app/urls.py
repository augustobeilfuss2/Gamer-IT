
"""
Definition of urls for Teste.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path
from app.views import (ListaPlayers, PlayerCreateView, CursosCreateView, InsereCursosForm, IndexTemplateView, ListaCursos, 
PlayerUpdate, CursosUpdate, PlayerDelete, CursoDelete
)
app_name = 'app'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('admin/', admin.site.urls),

    path('createP/', views.post_createPlayer, name="cadastra_player"),
    path('players/', ListaPlayers.as_view(), name ='lista_player'),
    path('players/<pk>', PlayerUpdate.as_view(), name ='update_player'),
    path('players/Delete/<pk>', PlayerDelete.as_view(), name ='delete_player'),


    path('createC/', views.post_create,  name="cadastra_curso"),
    path('cursos/', ListaCursos.as_view(), name ='lista_curso'),
    path('cursos/<pk>', CursosUpdate.as_view(), name ='update_curso'),
    path('cursos/Delete/<pk>', CursoDelete.as_view(), name ='delete_curso')   
    
]
