import django
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import CalcBinForms
from .models import Calculo
from .functions_bin import *

# Create your views here.

class CalcBinView(CreateView):
    template_name = "calc/calculator.html"
    model = Calculo
    form_class = CalcBinForms
    context_object_name = "calculadora"
    success_url = reverse_lazy("calc:result")

class ResultView(TemplateView):
    template_name = "calc/result.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        ultima = len(Calculo.objects.all())

        sentenca = Calculo.objects.filter(id=ultima)[0]
        content["sentenca"] = sentenca
        content["resultado"] = ""

        for elemento in str(sentenca):
            if elemento not in " +-/*01":
                content["resultado"] = "Sentença inválida"
                break
        
        if not content["resultado"]:
            content["resultado"] = resolve_equacao(str(sentenca))

        return content


