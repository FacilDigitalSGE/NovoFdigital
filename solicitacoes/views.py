from django.shortcuts import render
from django.utils.safestring import mark_safe


def criar_solicitacao(request):
    return render(request, 'solicitacoes/criar_solicitacao.html')

def protocolo_novo_pedido(request):
    return render(request, 'solicitacoes/protocolo_novo_pedido.html')

from django.shortcuts import render

def solicitacoes_analise(request):
    return render(request, 'solicitacoes/solicitacoes_analise.html')

def classificacao_solicitacao(request):
    return render(request, 'solicitacoes/classificacao_solicitacao.html')

  
def minhas_solicitacoes(request):
    def get_status_html(status):
        status_mapping = {
            'Aguardando Análise': ('fas fa-info-circle', 'br-tag info'),
            'Em análise': ('fas fa-search', 'br-tag warning'),
            'Concluída': ('fas fa-check-circle', 'br-tag success'),
            'Encaminhada': ('fas fa-check-circle', 'br-tag success'),
            'Com Pendência': ('fas fa-exclamation-circle', 'br-tag warning'),
            'Cancelada': ('fas fa-times-circle', 'br-tag danger'),
            'Cancelada pelo Sistema': ('fas fa-times-circle', 'br-tag danger'),
            'Cancelada pelo Usuário': ('fas fa-times-circle', 'br-tag danger')
        }

        icon_class, tag_class = status_mapping.get(status, ('fas fa-info-circle', 'br-tag info'))
        html = f'<span class="{tag_class}"><i class="{icon_class}"></i> {status}</span>'
        return mark_safe(html)

    table_data = [
        ["54321", get_status_html("Aguardando Análise"), "Requerimento de Alvará", "10/10/2024"],
        ["13579", get_status_html("Em análise"), "Solicitação de Licença", "29/09/2024"],
        ["13579", get_status_html("Com Pendência"), "Pedido de Isenção", "28/09/2024"],
        ["33445", get_status_html("Encaminhada"), "Autorização para Obra", "12/09/2024"],
        ["55667", get_status_html("Cancelada pelo Usuário"), "Cancelamento de Contrato", "10/09/2024"],
        ["77889", get_status_html("Cancelada pelo Sistema"), "Solicitação de Transferência", "01/09/2024"],
        ["11223", get_status_html("Concluída"), "Renovação de Licença", "15/09/2024"]
    ]

    return render(request, 'solicitacoes/minhas_solicitacoes.html', {
        'table_data': table_data,
        'columns': ["Inscrição/Cadastro", "Situação", "Assunto", "Data Solicitação"]
    })

def aguardando_analise(request):
    # Dados fictícios para demonstração
    dados_solicitacao = {
        'protocolo': '76550',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Solicitação de Serviços Teste',
        'data_solicitacao': '18/10/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '18/10/2024'
        }
    }
    return render(request, 'solicitacoes/aguardando_analise.html', dados_solicitacao)

def em_analise(request):
    dados_solicitacao = {
        'protocolo': '13579',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Solicitação de Serviços Teste',
        'data_solicitacao': '18/10/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '18/10/2024'
        }
    }
    return render(request, 'solicitacoes/em_analise.html', dados_solicitacao)

def com_pendencia(request):
    dados_solicitacao = {
        'protocolo': '13579',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Pedido de Isenção',
        'data_solicitacao': '28/09/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '28/09/2024'
        }
    }
    return render(request, 'solicitacoes/com_pendencia.html', dados_solicitacao)

def encaminhada(request):
    dados_solicitacao = {
        'protocolo': '33445',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Autorização para Obra',
        'data_solicitacao': '12/09/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '12/09/2024'
        }
    }
    return render(request, 'solicitacoes/encaminhada.html', dados_solicitacao)

def cancelada_usuario(request):
    dados_solicitacao = {
        'protocolo': '24680',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Solicitação de Certidão',
        'data_solicitacao': '15/10/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '15/10/2024'
        }
    }
    return render(request, 'solicitacoes/cancelada_usuario.html', dados_solicitacao)

def cancelada_sistema(request):
    dados_solicitacao = {
        'protocolo': '98765',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Solicitação de Certidão',
        'data_solicitacao': '01/10/2024',
        'documento': {
            'nome': 'MATRICULA',
            'tipo': 'application/pdf',
            'data': '01/10/2024'
        }
    }
    return render(request, 'solicitacoes/cancelada_sistema.html', dados_solicitacao)

def concluida(request):
    dados_solicitacao = {
        'protocolo': '44556',
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'assunto': 'Certidão Negativa',
        'data_solicitacao': '10/10/2024',
        'documento': {
            'nome': 'CERTIDÃO',
            'tipo': 'application/pdf',
            'data': '18/10/2024'
        }
    }
    return render(request, 'solicitacoes/concluida.html', dados_solicitacao)

def solicitacoes_para_analise(request):
    table_data = [
        ["78550", "Análise de Documentos", "22/10/2024", "João Silva", "123.456.789-00", "(11) 98765-4321", "joao@email.com", "20/10/2024", {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': True, 'urgent': False}}}],
        ["78551", "Renovação de Licença", "23/10/2024", "Maria Santos", "987.654.321-00", "(11) 91234-5678", "maria@email.com", "21/10/2024", {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': False, 'urgent': True}}}],
        ["78552", "Alteração Cadastral", "24/10/2024", "Pedro Alves", "456.789.123-00", "(11) 94567-8901", "pedro@email.com", "22/10/2024", {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': True, 'urgent': True}}}]
    ]

    columns = ["Nº Protocolo", "Assunto", "Data Atribuição", "Solicitante", "CPF/CNPJ", "Telefone", "E-mail", "Data Entrada", "Prioridade"]

    return render(request, 'solicitacoes/solicitacoes_para_analise.html', {
        'table_data': table_data,
        'columns': columns
    })
    
def analisar_solicitacao(request):
    dados_solicitacao = {
        'solicitante': 'SILMAR APARECIDO NEVES MORENO',
        'inscricao': '123.45.66.0666.0',
        'cadastro': '4566',
        'data_hora': '18/10/2024 15:45:36',
        'status': 'Em Análise'
    }
    return render(request, 'solicitacoes/analisar_solicitacao.html', dados_solicitacao)

def novas_solicitacoes(request):
    table_data = [
        ["78550", "Análise de Documentos", "22/10/2024", "João Silva", "123.456.789-00", 
         "(11) 98765-4321", "joao@email.com", "20/10/2024", 
         {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': True, 'urgent': False}}}],
        ["78551", "Renovação de Licença", "23/10/2024", "Maria Santos", "987.654.321-00",
         "(11) 91234-5678", "maria@email.com", "21/10/2024",
         {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': False, 'urgent': True}}}],
        ["78552", "Alteração Cadastral", "24/10/2024", "Pedro Alves", "456.789.123-00",
         "(11) 94567-8901", "pedro@email.com", "22/10/2024",
         {'template': 'components/priority_column.html', 'context': {'priority': {'elderly': False, 'urgent': False}}}]
    ]

    return render(request, 'solicitacoes/novas_solicitacoes.html', {
        'table_data': table_data
    })
