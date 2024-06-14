from django import forms
from .models import Persona,Grupo
from .choices import rol,sexo

class PersonaForm (forms.ModelForm):
    class Meta:
        model=Persona
        fields='__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=sexo),
            'rol': forms.Select(choices=rol),
            #'grupo': forms.CheckboxSelectMultiple(),  # Para manejar ManyToMany como checkboxes
            'grupo': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        
        grupo = forms.ModelMultipleChoiceField(
        queryset=Grupo.objects.all(),
        widget=forms.SelectMultiple,  # o forms.CheckboxSelectMultiple si prefieres checkboxes
        required=False
        )

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].required = False  # Permitir valores en blanco
        self.fields['imagen'].required = False

class GrupoForm (forms.ModelForm):
    class Meta:
        model=Grupo
        fields='__all__'