from django.urls import path
from . import views

app_name = 'distribuicao'

urlpatterns = [
    path('criar-classificacao/', views.criar_classificacao, name='criar_classificacao'),
    path('nova-classificacao/', views.nova_classificacao, name='nova_classificacao'),
    path('criar-rota/', views.criar_rota, name='criar_rota'),
    path('editar_rota/', views.editar_rota, name='editar_rota'),
    path('configurar-distribuicao/', views.configurar_distribuicao, name='configurar_distribuicao'),


]
