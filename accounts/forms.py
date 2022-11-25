from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class GuestForm(forms.Form):
    email = forms.EmailField()
    
class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': _('Usuário')}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': _('Senha')}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': _('Usuário')}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': _('Senha')}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': _('Confirme sua senha')}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(_("Esse usuário já existe, escolha outro nome."))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(_("Esse email já existe, tente outro!"))
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError(_("As senhas informadas devem ser iguais!"))
        return data