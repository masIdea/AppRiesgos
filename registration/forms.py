from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, pruebe con otro.")
        return email


