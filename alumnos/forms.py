from django import forms
from .models import Genero, Alumno

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"
    
    def clean_nombre_genero(self):
        genero = self.cleaned_data.get('genero')
        if Genero.objects.filter(genero=genero).exists():
            raise forms.ValidationError('Este género ya existe.')
        return genero