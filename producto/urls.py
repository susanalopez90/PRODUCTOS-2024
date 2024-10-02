#Estas son las urls a utilizar para mi aplicacion de producto 

from django.urls import path
from producto import views

urlpatterns = [
   path('hola mundo', views.hola_mundo),
   path('', views.inicio)
]