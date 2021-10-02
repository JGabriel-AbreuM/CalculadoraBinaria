from django.urls import path
from .views import CalcBinView, ResultView

app_name = "calc"

urlpatterns = [
    path('', CalcBinView.as_view(), name="calculadora_binario"),
    path('resultado/', ResultView.as_view(), name="result")
]
