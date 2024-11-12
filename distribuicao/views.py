from django.shortcuts import render

def nova_classificacao(request):
    return render(request, 'distribuicao/nova_classificacao.html')
def criar_classificacao(request):
    from django.template.loader import render_to_string
    
    columns = ["Descrição", "Ativo", "Data de Inclusão", "Ações"]
    table_data = []
    
    # Dados fictícios para demonstração
    classificacoes = [
        {
            'descricao': 'ESPECÍFICO LICENÇA, VRE, CLI',
            'ativo': True,
            'data_inclusao': '07/11/2024'
        },
        {
            'descricao': 'ISS, ITBI, PROTESTO, OBRA',
            'ativo': True,
            'data_inclusao': '07/11/2024'
        },
        {
            'descricao': 'ESPECÍFICO VISA, MEIO AMBIENTE',
            'ativo': False,
            'data_inclusao': '07/11/2024'
        }
    ]
    
    for c in classificacoes:
        row = [
            f'<div class="text-center">{c["descricao"]}</div>',
            f'<div class="text-center"><span class="br-tag {"success" if c["ativo"] else "danger"}">{("Sim" if c["ativo"] else "Não")}</span></div>',
            f'<div class="text-center">{c["data_inclusao"]}</div>',
            '''<div class="text-center">
                <button class="br-button secondary circle small" type="button" title="Editar">
                    <i class="fas fa-edit" aria-hidden="true"></i>
                </button>
                <button class="br-button danger circle small" type="button" title="Excluir">
                    <i class="fas fa-trash" aria-hidden="true"></i>
                </button>
            </div>'''
        ]
        table_data.append(row)

    context = {
        'title': 'Classificações Cadastradas',
        'columns': columns,
        'table_data': table_data,
        'grid_id': 'classificacoes'
    }
    
    grid = render_to_string('components/ggrid.html', context)
    
    return render(request, 'distribuicao/criar_classificacao.html', {'grid': grid})
def criar_rota(request):
    from django.template.loader import render_to_string
    
    # Dados fictícios para classificações e grupos pré-cadastrados
    classificacoes = [
        {'id': 1, 'descricao': 'Classificação 1'},
        {'id': 2, 'descricao': 'Classificação 2'},
        {'id': 3, 'descricao': 'Classificação 3'},
    ]
    
    columns = ["Ordem", "Descrição", "Ativo", "Data Inclusão", "Ações"]
    table_data = []
    
    grupos = [
        {'id': 1, 'ordem': 1, 'descricao': '4 - ESPECÍFICO DRM, SSP, CERTIDOES (Emitidas pelo Fácil)', 'ativo': 'Sim', 'data_inclusao': '02/04/2024'},
        {'id': 2, 'ordem': 2, 'descricao': '6 - ESPECÍFICO LICENÇA, VRE, CLI', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 3, 'ordem': 3, 'descricao': '3 - ISS, ITBI, PROTESTO, OBRA', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 4, 'ordem': 4, 'descricao': '5 - ESPECÍFICO VISA, MEIO AMBIENTE', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 5, 'ordem': 5, 'descricao': '2', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 6, 'ordem': 6, 'descricao': '1', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
    ]

    for g in grupos:
        row = [
            f'<div class="text-center">{g["ordem"]}</div>',
            f'<div class="text-center">{g["descricao"]}</div>',
            f'<div class="text-center">{g["ativo"]}</div>',
            f'<div class="text-center">{g["data_inclusao"]}</div>',
            f'''<div class="text-center">
                <button type="button" class="br-button circle" onclick="visualizarGrupo({g['id']})">
                    <i class="fas fa-eye" aria-hidden="true"></i>
                </button>
                <button type="button" class="br-button circle" onclick="window.location.href='http://127.0.0.1:8000/distribuicao/editar_rota/'">
                    <i class="fas fa-edit" aria-hidden="true"></i>
                </button>
            </div>'''
        ]
        table_data.append(row)

    context = {
        'title': 'Grupos Pré-cadastrados',
        'columns': columns,
        'table_data': table_data,
        'grid_id': 'grupos'
    }
    
    grid = render_to_string('components/ggrid.html', context)
    
    return render(request, 'distribuicao/criar_rota.html', {
        'classificacoes': classificacoes,
        'grid': grid
    })


def editar_rota(request):
    # Esta função simplesmente renderiza o template editar_rota.html sem dados adicionais
    return render(request, 'distribuicao/editar_rota.html')


def configurar_distribuicao(request):
    from django.template.loader import render_to_string
    
    # Tabela de Estatísticas
    columns_estatisticas = ["Complexidade", "Quantidade", "Atendentes", "Média Atendente"]
    table_data_estatisticas = [
        ['<div class="text-center">2</div>', 
         '<div class="text-center">67</div>', 
         '<div class="text-center">42</div>', 
         '<div class="text-center">1,59</div>'],
        ['<div class="text-center">4 - ESPECÍFICO DRM, SSP, CERTIDOES</div>', 
         '<div class="text-center">82</div>', 
         '<div class="text-center">13</div>', 
         '<div class="text-center">6,31</div>'],
        ['<div class="text-center">5 - ESPECÍFICO VISA, MEIO AMBIENTE</div>', 
         '<div class="text-center">38</div>', 
         '<div class="text-center">7</div>', 
         '<div class="text-center">5,42</div>'],
        ['<div class="text-center">6 - ESPECÍFICO LICENÇA, VRE, CLI</div>', 
         '<div class="text-center">14</div>', 
         '<div class="text-center">5</div>', 
         '<div class="text-center">2,80</div>'],
        ['<div class="text-center"><strong>Total</strong></div>', 
         '<div class="text-center">201</div>', 
         '<div class="text-center">70</div>', 
         '<div class="text-center">2,87</div>']
    ]
    
    # Tabela de Configurações por Atendente
    columns_atendentes = ["Classificação", "Usuário", "Departamento", "Entrega Automática", "Retorno Automático", "Desabilitar % Superior"]
    table_data_atendentes = [
        ['<div class="text-center">2</div>',
         '<div class="text-center">ADAILSILVA</div>',
         '<div class="text-center">Fácil Bom Clima Tarde</div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="entrega1"><label for="entrega1"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="retorno1"><label for="retorno1"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="superior1"><label for="superior1"></label></div></div>'],
        ['<div class="text-center">4</div>',
         '<div class="text-center">MARIASILVA</div>',
         '<div class="text-center">Fácil Centro Manhã</div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="entrega2" checked><label for="entrega2"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="retorno2" checked><label for="retorno2"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="superior2"><label for="superior2"></label></div></div>'],
        ['<div class="text-center">3</div>',
         '<div class="text-center">JOAOSANTOS</div>',
         '<div class="text-center">Fácil Pimentas Tarde</div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="entrega3"><label for="entrega3"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="retorno3" checked><label for="retorno3"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="superior3" checked><label for="superior3"></label></div></div>'],
        ['<div class="text-center">5</div>',
         '<div class="text-center">ANALUIZA</div>',
         '<div class="text-cente    r">Fácil São João Manhã</div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="entrega4" checked><label for="entrega4"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="retorno4"><label for="retorno4"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="superior4"><label for="superior4"></label></div></div>'],
        ['<div class="text-center">2</div>',
         '<div class="text-center">PEDROHENRIQUE</div>',
         '<div class="text-center">Fácil Centro Tarde</div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="entrega5" checked><label for="entrega5"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="retorno5" checked><label for="retorno5"></label></div></div>',
         '<div class="text-center"><div class="br-switch small"><input type="checkbox" id="superior5" checked><label for="superior5"></label></div></div>']
    ]
 

    context_estatisticas = {
        'title': 'Estatísticas das Solicitações Não Distribuídas',
        'columns': columns_estatisticas,
        'table_data': table_data_estatisticas,
        'grid_id': 'estatisticas'
    }
    
    context_atendentes = {
        'title': 'Configurações por Atendente',
        'columns': columns_atendentes,
        'table_data': table_data_atendentes,
        'grid_id': 'atendentes'
    }
    
    grid_estatisticas = render_to_string('components/ggrid.html', context_estatisticas)
    grid_atendentes = render_to_string('components/ggrid.html', context_atendentes)

    
    return render(request, 'distribuicao/configurar_distribuicao.html', {
        'grid_estatisticas': grid_estatisticas,
        'grid_atendentes': grid_atendentes
    })
