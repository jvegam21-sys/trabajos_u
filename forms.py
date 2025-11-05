from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'edad', 'correo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError("El nombre no puede contener números.")
        return nombre

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 5:
            raise forms.ValidationError("La edad debe ser mayor o igual a 5 años.")
        return edad
