"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Players, Cursos

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class InserePlayerForm(forms.ModelForm):


    class Meta:
        # Modelo base
        model = Players

        # Campos que estar�o no form
        fields = [
            'nmcolaborador',
            'imcolaborador',
            'nmSetor',
        ]



class InsereCursosForm(forms.ModelForm):



    class Meta:
        # Modelo base
        model = Cursos

        # Campos que estar�o no form
        fields = [
            'nmCurso',
            'acFaculdade',
            'nuMaterias',
            'nmInstituicao',
            'nmPlayer',
            'nuHoras',
            'acWorkshop',
            'acImplementacao',
            'acComunik'
        ]
        