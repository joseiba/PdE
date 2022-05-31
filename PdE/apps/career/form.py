from django import forms

from apps.career.models import Career, Semester


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(attrs={'id':'name','autocomplete': 'off',
                'name': 'name', 'placeholder': 'Nombre de la Carrera', 'type':'text','class':'form-control', 'required': 'required'}),
            'description' : forms.Textarea(attrs={'class':'','autocomplete': 'off',
                'name': 'description', 'placeholder': 'Descripcion',}),
        }


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(attrs={'id':'name','autocomplete': 'off',
                'name': 'name', 'placeholder': 'Nombre del Semestre', 'type':'text','class':'form-control', 'required': 'required'}),
            'description' : forms.Textarea(attrs={'class':'','autocomplete': 'off',
                'name': 'description', 'placeholder': 'Descripcion',}),
            'id_career' : forms.HiddenInput(),
        }