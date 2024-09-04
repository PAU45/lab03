from django import forms
from .models import Propietario, Vehiculo, Registro

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'numero_apartamento', 'telefono', 'email']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['matricula', 'marca', 'modelo', 'color', 'propietario']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['vehiculo', 'fecha_hora_entrada', 'fecha_hora_salida']
        widgets = {
            'fecha_hora_entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_salida': forms.DateTimeInput(attrs={'type': 'datetime-local', 'required': False}),
        }