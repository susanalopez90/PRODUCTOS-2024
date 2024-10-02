from django.shortcuts import render
#importamos HttpResponse
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
#Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>hola mundo desde mi aplicacion Web</h1><br><p>Esta es una prueba de párrafo</p>")

#crear vista principal
def inicio(request):
    return render(request,'base.html')