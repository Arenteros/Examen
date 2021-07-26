from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm, fields
from django import forms
from django.db import models
from django.forms import ModelForm, fields
from .models import Producto, suscriptor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import TamañoMaximoValidator

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5, max_length=80)
    precio = forms.IntegerField(min_value= 5000)
    descripcion = forms.CharField(min_length=5, max_length=200)
    imagen = forms.ImageField(validators=[TamañoMaximoValidator(3)], required=False)

    def clean_nombre(self):
        nom = self.cleaned_data["nombre"]
        aux = Producto.objects.filter(nombre__iexact=nom).exists()

        if aux:
            raise ValidationError("Este producto ya existe")

        return nom  

    class Meta:
        model = Producto
        fields = '__all__'
        fields = ['nombre','precio','descripcion', 'tipo', 'imagen']


class UsuarioCreationForm(UserCreationForm):

    def clean_user(self):
        use = self.cleaned_data["username"]
        aux = Producto.objects.filter(nombre__iexact=use).exists()

        if aux:
            raise ValidationError("Este usuario ya existe")

        return use 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class suscriptorForm(ModelForm):

    class Meta:
        model = suscriptor
        fields = ['nombre','correo','tipo_pago','monto_donacion']

