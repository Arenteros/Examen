from django.contrib.auth import authenticate, login
from django.core import paginator
from app.forms import ProductoForm, UsuarioCreationForm, suscriptorForm
from app.models import Producto
from django.shortcuts import render, redirect 
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.

def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listasProductos' : productosAll,
    }
    return render(request, 'app/index.html', datos)
    

def producto(request):
    productosAll = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productosAll, 5)
        productosAll = paginator.page(page)
    except:
        raise Http404

    datos = {
        'listasProductos' : productosAll,
        'paginator' : paginator
    }
    return render(request, 'app/producto.html', datos)

def quienes(request):
    return render(request, 'app/quienes.html')

def registro_usuario(request):
    datos = {
        'form' : UsuarioCreationForm()
    }

    if request.method == 'POST':
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        datos['form'] = formulario

    return render(request, 'registration/signup.html', datos)

def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"

        datos['form'] = formulario

    return render(request, 'app/agregar_producto.html', datos)

def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="producto")

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def suscriptor (request):
    data ={ 
        'form' : suscriptorForm()
    } 

    if request.method == 'POST':
        formulario = suscriptorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data['form'] = formulario

    return render(request,'app/suscripcion.html',data)
    