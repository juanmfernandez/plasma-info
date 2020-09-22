from django import forms
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#Realizamos una clase para cada formulario que nosotros querramos simpre que este pertenezca a models.

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'dni', 'fecha_nac', )
        #'user_permissions'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarme'))
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Nombre', 'placeholder': 'usuario'})
        self.fields['password'] = forms.CharField(max_length=20, widget=forms.PasswordInput())
        #self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'placeholder': 'contraseña'})
        #self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'placeholder': 'repetir contraseña'})
        self.fields['dni'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'aria-describedby': 'basic-addon3'})
        self.fields['fecha_nac'].widget.attrs.update({'class': 'form-control', 'type': 'date'})



