from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor

class ProveedorRegistroForm(UserCreationForm):
    #rut_cliente = forms.CharField(label="RUT Cliente", max_length=12, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT Cliente'}))
    nombre_proveedor = forms.CharField(label="Nombre proveedor", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre visible en las publicaciones'}))
    fono_proveedor = forms.DecimalField(label="Telefono contacto", max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telefono contacto del proveedor'}))
    
    #direccion_cliente = forms.CharField(label="Dirección Cliente", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección Cliente'}))
    username = forms.CharField(label="Usuario", max_length=150, help_text="Obligatorio. debe contener menos de 150 characters or fewer. Letters, digits and @/./+/-/_ only.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de usuario para iniciar sesion'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}))
    email_proveedor = forms.EmailField(label="Correo Electrónico", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    first_name = forms.CharField(label="Nombre persona contacto", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Persona que gestiona la cuenta'}))
    last_name = forms.CharField(label="Apellido persona contacto", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido de la persona de contacto'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email_proveedor', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email_proveedor']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

            proveedor = Proveedor.objects.create(
                user=user,
                #nombre_persona=user.first_name,
                #apellido_persona=user.last_name,
                nombre_proveedor=self.cleaned_data['nombre_proveedor'],
                fono_proveedor=self.cleaned_data['fono_proveedor'],
                #empresa=self.cleaned_data['empresa'],
                #direccion_cliente=self.cleaned_data['direccion_cliente']
            )

        return user