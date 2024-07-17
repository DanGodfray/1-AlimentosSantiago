from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Repartidor

class RepartidorRegistroForm(UserCreationForm):
    #rut_cliente = forms.CharField(label="RUT Cliente", max_length=12, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT Cliente'}))
    rut_repartidor = forms.CharField(label="Rut repartidor", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre visible en las entregas '}))
    fono_repartidor = forms.CharField(label="Telefono contacto", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'telefono de contacto'}))
    
    #direccion_cliente = forms.CharField(label="Dirección Cliente", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección Cliente'}))
    username = forms.CharField(label="Usuario", max_length=150, help_text="Obligatorio. debe contener menos de 150 characters or fewer. Letters, digits and @/./+/-/_ only.", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese usuario para iniciar sesion'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}))
    email_repartidor= forms.EmailField(label="Correo Electrónico", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    first_name = forms.CharField(label="Nombre", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Persona que gestiona la cuenta'}))
    last_name = forms.CharField(label="Apellido", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido de la persona de contacto'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email_repartidor', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email_repartidor']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            Repartidor.objects.create(
                user=user,
                rut_repartidor=self.cleaned_data['rut_repartidor'],
                fono_repartidor=self.cleaned_data['fono_repartidor']
            )

        return user