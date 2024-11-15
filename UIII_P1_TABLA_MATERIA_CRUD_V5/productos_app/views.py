from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.
def inicio_vista(request):
    losProductos=Productos.objects.all()
    return render (request,"gestionarProductos.html", {"misProductos":losProductos})

def registrarProducto(request):
    IdProducto=request.POST["txtcodigo"]
    Nombre=request.POST["txtnombre"]
    Stock=request.POST["numcreditos"]
    Proveedor=request.POST["txtProveedor"]
    PrecioVenta=request.POST["numPrecioVenta"]
    PrecioMayoreo=request.POST["numPrecioMayoreo"]
    Descripcion=request.POST["txtDescripcion"]





    guardarProducto=Productos.objects.create(
        IdProducto=IdProducto,Nombre=Nombre,Stock=Stock, Proveedor=Proveedor, PrecioVenta=PrecioVenta, PrecioMayoreo=PrecioMayoreo, Descripcion=Descripcion
    ) # GUARDA EL REGISTRO

    return redirect("/")

def seleccionarProducto(request,codigo):
    Productos=Productos.objects.get(codigo=codigo)
    return render(request,"editarProductos.html",{"misProductos":Productos})

def editarProducto(request):
    IdProducto=request.POST["txtcodigo"]
    Nombre=request.POST["txtnombre"]
    Stock=request.POST["numcreditos"]
    Proveedor=request.POST["txtProveedor"]
    PrecioVenta=request.POST["numPrecioVenta"]
    PrecioMayoreo=request.POST["numPrecioMayoreo"]
    Descripcion=request.POST["txtDescripcion"]

    productos=Productos.objects.get(IdProducto=IdProducto)
    productos.Nombre=Nombre
    productos.Stock=Stock
    productos.Proveedor=Proveedor
    productos.PrecioVenta=PrecioVenta
    productos.PrecioMayoreo=PrecioMayoreo
    productos.Descripcion=Descripcion
    productos.save() #guardar registro actualizado
    return redirect("/")

def borrarProducto(request,IdProducto):
    producto=Productos.objects.get(IdProducto=IdProducto)
    producto.delete()
    return redirect("/")

