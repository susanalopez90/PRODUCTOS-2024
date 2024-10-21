from django.shortcuts import render

# Vista de inicio
def inicio(request):
    autenticado = False
    usuario = "SUSANA LOPEZ"
    contexto = {
        "esta_autenticado": autenticado,
        "user": usuario
    }
    return render(request, 'page/index.html', contexto)

# Vista de productos
def productos(request):
    productos = []
    for i in range(5):
        producto = {
            "nombre": "coca-cola",
            "precio": 0.75,
            "iva": 0.75*0.13,
            "cantidad": 24
        }
        productos.append(producto)
    
    # Incluye el nombre del usuario en el contexto
    usuario = "SUSANA LOPEZ"
    contexto = {
        "productos": productos,
        "user": usuario
    }
    return render(request, 'page/productos.html', contexto)
