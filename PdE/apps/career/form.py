from tkinter import Widget
from django import forms

from apps.career.models import Career


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(attrs={'class':'form-control','autocomplete': 'off',
                'name': 'name', 'placeholder': 'Nombre de la Carrera', 'type':'text','required': 'required'}),
            'desciption' : forms.Textarea(attrs={'class':'','autocomplete': 'off',
                'name': 'desciption', 'placeholder': 'Descripcion',}),
        }