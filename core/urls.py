"""--> ARQUIVO DE CONFIGURAÇÃO DE ROTAS(URLS) QUE RETORNAM UM MÉTODO NO ARQUIVO Views.py RESPONSÁVEL POR RENDERIZAR
A PAGINA RELATIVA A ROTA ESPECIFICADA
"""
from django_ubs.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core.views import index, contato, senhas, agenda, dependente, endereco, filiacao, paciente  # - Importando métodos(de renderização da pagina) do arquivo views para 'urls.py'


urlpatterns = [
    path('', index, name='index'),  # Rota para o método 'index' que retorna 'index.html'
    path('contato', contato, name='contato'),
    path('senhas', senhas, name='senhas'),
    path('agenda', agenda, name='agenda'),
    path('dependente', dependente, name='dependente'),
    path('endereco', endereco, name='endereco'),
    path('filiacao', filiacao, name='filiacao'),
    path('paciente', paciente, name='paciente')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
