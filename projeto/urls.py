from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('solicitacoes/', include('solicitacoes.urls')),
    path('distribuicao/', include('distribuicao.urls', namespace='distribuicao')),
    path('relatorios/', include('relatorios.urls', namespace='relatorios')),
    path('pesquisa/', include('pesquisa.urls')),
]



