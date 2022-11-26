from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()
class ContactForm(forms.Form):
    full_name = forms.CharField(label=".",
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": _("Seu nome completo")
                }
            )
        )
    email     = forms.EmailField(label=".",
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": _("Digite seu e-mail")
                }
            )
        )
    content   = forms.CharField(label=".",
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": _("Digite sua mensagem")
                }
            )
        )
    