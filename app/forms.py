"""
Definition of forms.
"""
from dataclasses import fields
from .models import Vacancies, UserClient, Candidato


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class VacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ["titulo", "descricao", "salario", "empresa",
                  "modalidade", "local", "tecnologias", "tipo_contratacao", ]


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ["empresa", "usuario"]


class UserClassForm(forms.ModelForm):
    class Meta:
        model = UserClient
        fields = ["full_name", "birthday", "scholarity", "cpf", "telephone_number",
                  "city", "district", "street", "numero_usuario", "email", "password", "document"]
        widget = {
            'password': forms.PasswordInput()
        }
