from django import forms
from .models import Autor
from .models import Post, Comentario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#Realizamos una clase para cada formulario que nosotros querramos simpre que este pertenezca a models.

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombres',
                 'apellidos',
                 'email',
                 'facebook',
                 'instagram',
                 'donante']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar'))
        self.fields['nombres'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Nombre', 'placeholder': 'José'})
        self.fields['apellidos'].widget.attrs.update({'class': 'form-control', 'aria-label': 'Apellido', 'placeholder': 'Soto'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email', 'id': 'basic-url', 'aria-label': 'Email', 'placeholder': 'nn@mail.com'})
        self.fields['facebook'].widget.attrs.update({'class': 'form-control', 'id': 'basic-url', 'aria-describedby': 'basic-addon3', 'value': 'facebook.com/'})
        self.fields['instagram'].widget.attrs.update({'class': 'form-control', 'id': 'basic-url', 'aria-describedby': 'basic-addon3', 'value': 'instagram.com/'})
        self.fields['donante'].widget.attrs.update({'value': 'Donante'})


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'contenido',)


