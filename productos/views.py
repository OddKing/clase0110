from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def electronica(request):
    data={
        'titulo':'Electronica',
        'Producto1':'mac',
        'Producto2':'Celular',
        'Producto3':'Playstation'
    }
    return render(request,'Productos.html',data)

def juguetes(request):
    data={
        'titulo':'Juguetes',
        'Producto1':'pelota',
        'Producto2':'Figura Accion',
        'Producto3':'Juegos de mesa',
    }
    return render(request,'Productos.html',data)

def ropa(request):
    data={
        'titulo':'Ropa',
        'Producto1':'Polera',
        'Producto2':'Chaqueta',
        'Producto3':'Zapatilla',
    }
    return render(request,'Productos.html',data)