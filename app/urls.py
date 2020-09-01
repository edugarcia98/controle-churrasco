from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('participar-churrasco/', views.ParticiparChurrasco.as_view()),
    path('funcionarios/', views.ShowFuncionarios.as_view()),
    path('convidados/', views.ShowConvidados.as_view()),
    path('cancelar-participacao/<int:pk>/', views.CancelarParticipacao.as_view()),
    path('total-arrecadado/', views.TotalArrecadado.as_view()),
    path('compras/', views.CompraView.as_view()),
    path('compras/<int:pk>/', views.CompraDetail.as_view()),
    path('total-compras/', views.TotalGastoCompra.as_view()),
    path('total-compras/comida/', views.TotalGastoCompra.as_view()),
    path('total-compras/bebida/', views.TotalGastoCompra.as_view())
]
