from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('criar/', views.criar_solicitacao, name='criar_solicitacao'),
    path('protocolo/', views.protocolo_novo_pedido, name='protocolo_novo_pedido'),
    path('analise/', views.solicitacoes_analise, name='solicitacoes_analise'),
    path('classificacao/', views.classificacao_solicitacao, name='classificacao_solicitacao'),
    path('minhas-solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('aguardando-analise/', views.aguardando_analise, name='aguardando-analise'),
    path('em-analise/', views.em_analise, name='em-analise'),
    path('com-pendencia/', views.com_pendencia, name='com-pendencia'),
    path('encaminhada/', views.encaminhada, name='encaminhada'),
    path('cancelada-usuario/', views.cancelada_usuario, name='cancelada-usuario'),
    path('cancelada-sistema/', views.cancelada_sistema, name='cancelada-sistema'),
    path('concluida/', views.concluida, name='concluida'),
    path('novas_solicitacoes/', views.novas_solicitacoes, name='novas_solicitacoes'),
    path('analisar-solicitacao/', views.analisar_solicitacao, name='analisar_solicitacao'),
    path('solicitacoes_para_analise/', views.solicitacoes_para_analise, name='solicitacoes_para_analise'),
    # urls.py
    



]





