from django import forms
from .models import Calculo

class CalcBinForms(forms.ModelForm):
    class Meta:
        model = Calculo
        fields = ["sentenca"]