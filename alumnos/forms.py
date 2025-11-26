from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'edad', 'curso']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Pérez'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '120'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 5to año'}),
        }



