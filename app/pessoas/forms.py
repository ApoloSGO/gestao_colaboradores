from django import forms
from django.contrib.auth.models import User
from .models import Documento, Pessoa

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['telefone']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'arquivo']
