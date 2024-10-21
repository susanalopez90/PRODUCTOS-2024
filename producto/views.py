from django.shortcuts import render
from django.http import HttpResponse

# Vista de inicio
def inicio(request):
    return render(request, 'page/index.html')

# Vista de productos
def productos(request):
    productos = []
    for i in range(5):
        producto = {
            "nombre": "coca-cola",
            "precio": 0.75,
            "cantidad": 24
        }
        productos.append(producto)
    
    # Diccionario es una conexión de clave, valor
    contexto = {
        "productos": productos,
        "usuario": "SUSANA LOPEZ"
    }
    return render(request, 'page/productos.html', contexto)

