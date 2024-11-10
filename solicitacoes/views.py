from django.shortcuts import render
from django.utils.safestring import mark_safe


def criar_solicitacao(request):
    return render(request, 'solicitacoes/criar_solicitacao.html')

def protocolo_novo_pedido(request):
    return render(request, 'solicitacoes/protocolo_novo_pedido.html')

from django.shortcuts import render
def solicitacoes_analise(request):
    from django.template.loader import render_to_string
    
    columns = ["Protocolo", "Data", "Solicitante", "Assunto", "Status", "Ações"]
    
    table_data = [
        ["45678/2024", "05/08/2024", "FULANO DE TAL LTDA", "Alteração Cadastral", 
          '<div class="br-tag warning">Em Análise</div>',
          '<button class="br-button circle small" type="button" title="Visualizar" onclick="window.location.href=\'/solicitacoes/analisar-solicitacao\'"><i class="fas fa-eye"></i></button>'],
        ["45679/2024", "05/08/2024", "EMPRESA XYZ LTDA", "Certidão Negativa",
          '<div class="br-tag warning">Em Análise</div>',
          '<button class="br-button circle small" type="button" title="Visualizar" onclick="window.location.href=\'/solicitacoes/analisar-solicitacao\'"><i class="fas fa-eye"></i></button>']
    ]
    
    context = {
        'title': 'Lista de Solicitações',
        'columns': columns,
        'table_data': table_data
    }
    
    grid_content = render_to_string('components/ggrid.html', context)
    return render(request, 'solicitacoes/solicitacoes_analise.html', {'grid_content': grid_content})
def classificacao_solicitacao(request):
    from django.template.loader import render_to_string
    
    columns = ["Selecionar", "Protocolo", "Data", "Solicitante", "Assunto", "Classificação", "Ações"]
    
    table_data = [
        ['<div class="br-checkbox"><input id="check1" type="checkbox"/><label for="check1"></label></div>',
         "45678/2024", 
         "05/08/2024", 
         "FULANO DE TAL LTDA", 
         "Alteração Cadastral",
         '<div class="br-select"><select><option value="">Selecione</option><option value="drm">DRM VRE</option><option value="outros">ITBI/ISSQN</option></select></div>',
         '<button class="br-button secondary circle small" type="button" title="Editar Classificação"><i class="fas fa-edit"></i></button> <button class="br-button circle small" type="button" title="Visualizar" onclick="window.location.href=\'/solicitacoes/analisar-solicitacao\'"><i class="fas fa-eye"></i></button>']
    ]
    
    context = {
        'title': 'Solicitações para Classificar',
        'columns': columns,
        'table_data': table_data
    }
    
    grid_content = render_to_string('components/ggrid.html', context)
    return render(request, 'solicitacoes/classificacao_solicitacao.html', {'grid_content': grid_content})


  
def minhas_solicitacoes(request):
    from django.template.loader import render_to_string
    
    columns = ["Nº Protocolo", "Situação", "Assunto", "Data Solicitação"]
    
    table_data = [
        ['<a href="/solicitacoes/aguardando-analise" class="br-button secondary small"><i class="fas fa-search"></i>54321</a>',
         '<span class="br-tag info"><i class="fas fa-info-circle"></i> Aguardando Análise</span>',
         "Requerimento de Alvará",
         "10/10/2024"],
        ['<a href="/solicitacoes/em-analise" class="br-button secondary small"><i class="fas fa-search"></i>13579</a>',
         '<span class="br-tag warning"><i class="fas fa-search"></i> Em análise</span>',
         "Solicitação de Licença",
         "29/09/2024"],
        ['<a href="/solicitacoes/com-pendencia" class="br-button secondary small"><i class="fas fa-search"></i>13579</a>',
         '<span class="br-tag warning"><i class="fas fa-exclamation-circle"></i> Com Pendência</span>',
         "Pedido de Isenção",
         "28/09/2024"]
    ]
    
    context = {
        'title': 'Solicitações',
        'columns': columns,
        'table_data': table_data
    }
    
    grid_content = render_to_string('components/ggrid.html', context)
    return render(request, 'solicitacoes/minhas_solicitacoes.html', {'grid_content': grid_content})


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
    from django.template.loader import render_to_string
    
    columns = ["Protocolo", "Data", "Solicitante", "Assunto", "Status", "Prioridade", "Ações"]
    
    table_data = [
        ["45678/2024", "05/08/2024", "FULANO DE TAL LTDA", "Alteração Cadastral", 
         '<div class="br-tag info">Aguardando Análise</div>',
         '<div class="d-flex align-items-center justify-content-center"><span class="br-tag info mr-2" title="Idoso"><i class="fas fa-user-clock"></i>Idoso</span><div class="br-switch small"><input id="urgent-45678" type="checkbox" checked><label for="urgent-45678">Urgente</label></div></div>',
         '<button class="br-button circle small" type="button" title="Visualizar" onclick="window.location.href=\'/solicitacoes/analisar-solicitacao\'"><i class="fas fa-eye"></i></button>'],
        ["45679/2024", "05/08/2024", "EMPRESA XYZ LTDA", "Certidão Negativa",
         '<div class="br-tag info">Aguardando Análise</div>',
         '<div class="br-switch small"><input id="urgent-45679" type="checkbox"><label for="urgent-45679">Urgente</label></div>',
         '<button class="br-button circle small" type="button" title="Visualizar" onclick="window.location.href=\'/solicitacoes/analisar-solicitacao\'"><i class="fas fa-eye"></i></button>']
    ]
    
    context = {
        'title': 'Solicitações',
        'columns': columns,
        'table_data': table_data
    }
    
    grid_content = render_to_string('components/ggrid.html', context)
    return render(request, 'solicitacoes/solicitacoes_para_analise.html', {'grid_content': grid_content})

    
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

def teste_switch(request):
    return render(request, 'solicitacoes/teste_switch.html')

def teste_tabela(request):
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
        ["13579", get_status_html("Com Pendência"), "Pedido de Isenção", "28/09/2024"]
    ]
    
    columns = ["Protocolo", "Situação", "Assunto", "Data"]

    return render(request, 'solicitacoes/components/tabela_solicitacoes.html', {
        'table_data': table_data,
        'columns': columns
    })

# views.py
def lista_usuarios(request):
    from django.template.loader import render_to_string
    
    columns = ["Nome", "Email", "Status", "Último Acesso"]
    table_data = [
        ["João Silva", "joao@email.com", "Ativo", "10/01/2024"],
        ["Maria Santos", "maria@email.com", "Pendente", "08/01/2024"],
        ["Pedro Costa", "pedro@email.com", "Inativo", "05/01/2024"]
    ]
    
    context = {
        'title': 'Lista de Usuários',
        'columns': columns,
        'table_data': table_data
    }
    
    grid_content = render_to_string('components/ggrid.html', context)
    return render(request, 'solicitacoes/lista_usuarios.html', {'grid_content': grid_content})


def test_grid(request):
    from django.template.loader import render_to_string
    
    context = {
        'title': 'Teste Grid',
        'columns': ['Col1', 'Col2', 'Col3'],
        'table_data': [
            ['A1', 'B1', 'C1'],
            ['A2', 'B2', 'C2']
        ]
    }
    
    test_grid = render_to_string('components/ggrid.html', context)
    return render(request, 'test_grid.html', {'test_grid': test_grid})

