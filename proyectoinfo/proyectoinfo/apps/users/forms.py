from django import forms
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Realizamos una clase para cada formulario que nosotros querramos simpre que este pertenezca a models.

class UsuarioForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'dni', 'fecha_nac', 'grupo_sanguineo', 'factor_rh', 'es_donante' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarme'))
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Nombre', 'placeholder': 'usuario'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'nn@mail.com'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'placeholder': 'contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'placeholder': 'repetir contraseña'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Nombre', 'placeholder': 'Nombre'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Apellido', 'placeholder': 'Apellido'})
        self.fields['dni'].widget.attrs.update({'class': 'form-control', 'aria-describedby': 'basic-addon3'})
        self.fields['fecha_nac'].widget.attrs.update({'class': 'form-control', 'type': 'date'})

