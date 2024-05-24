from django import forms
from .models import Persona,Grupo


class PersonaForm (forms.ModelForm):
    class Meta:
        model=Persona
        fields='__all__'

class GrupoForm (forms.ModelForm):
    class Meta:
        model=Grupo
        fields='__all__'