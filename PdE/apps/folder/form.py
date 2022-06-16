from django import forms

from apps.folder.models import Folder


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'
        widget = {
            'name' : forms.TextInput(attrs={'id':'name','autocomplete': 'off',
                'name': 'name', 'placeholder': 'Nombre de la Carrera', 'type':'text','class':'form-control', 'required': 'required'}),
            'description' : forms.Textarea(attrs={'class':'','autocomplete': 'off',
                'name': 'description', 'placeholder': 'Descripcion',}),
            'link': forms.TextInput(attrs={'id':'link','autocomplete': 'off',
                'name': 'link', 'placeholder': 'https://example.com', 'type':'url','class':'form-control', 'required': 'required', 
                'pattern':'https://.*'}),
            'id_semester' : forms.HiddenInput(),
        }