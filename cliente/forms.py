from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class ClienteRegistroForm(UserCreationForm):
    rut_cliente = forms.CharField(label="RUT Cliente", max_length=12, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT Cliente'}))
    fono_cliente = forms.DecimalField(label="Fono Cliente", max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fono Cliente'}))
    empresa = forms.CharField(label="Empresa", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa'}))
    direccion_cliente = forms.CharField(label="Dirección Cliente", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección Cliente'}))
    username = forms.CharField(label="Usuario", max_length=150, help_text="Obligatorio. 150 caracteres or menos. Letras, digitos y solamente caracteres tipo: @/./+/-/_ .", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}))
    email = forms.EmailField(label="Correo Electrónico", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}))
    nombre_cliente = forms.CharField(label="Nombre", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    apellido_cliente = forms.CharField(label="Apellido", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nombre_cliente', 'apellido_cliente')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nombre_cliente']
        user.last_name = self.cleaned_data['apellido_cliente']
        if commit:
            user.save()

            cliente = Cliente.objects.create(
                user=user,
                nombre_cliente=user.first_name,
                apellido_cliente=user.last_name,
                rut_cliente=self.cleaned_data['rut_cliente'],
                fono_cliente=self.cleaned_data['fono_cliente'],
                empresa=self.cleaned_data['empresa'],
                direccion_cliente=self.cleaned_data['direccion_cliente']
            )

        return user