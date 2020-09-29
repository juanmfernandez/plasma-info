from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import EnableCenter


class EnableCenterForm(forms.ModelForm):
    class Meta:
        model = EnableCenter
        fields = ('name', 'mail', 'phone_num', 'address',
                  'location', 'business_hours')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()