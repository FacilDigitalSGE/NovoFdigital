from django.shortcuts import render

def nova_classificacao(request):
    return render(request, 'distribuicao/nova_classificacao.html')

def criar_classificacao(request):
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
    return render(request, 'distribuicao/criar_classificacao.html', {'classificacoes': classificacoes})

def criar_rota(request):
    # Dados fictícios para classificações e grupos pré-cadastrados
    classificacoes = [
        {'id': 1, 'descricao': 'Classificação 1'},
        {'id': 2, 'descricao': 'Classificação 2'},
        {'id': 3, 'descricao': 'Classificação 3'},
    ]
    
    grupos = [
        {'id': 1, 'ordem': 1, 'descricao': '4 - ESPECÍFICO DRM, SSP, CERTIDOES (Emitidas pelo Fácil)', 'ativo': 'Sim', 'data_inclusao': '02/04/2024'},
        {'id': 2, 'ordem': 2, 'descricao': '6 - ESPECÍFICO LICENÇA, VRE, CLI', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 3, 'ordem': 3, 'descricao': '3 - ISS, ITBI, PROTESTO, OBRA', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 4, 'ordem': 4, 'descricao': '5 - ESPECÍFICO VISA, MEIO AMBIENTE', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 5, 'ordem': 5, 'descricao': '2', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
        {'id': 6, 'ordem': 6, 'descricao': '1', 'ativo': 'Sim', 'data_inclusao': '25/09/2024'},
    ]
    
    return render(request, 'distribuicao/criar_rota.html', {
        'classificacoes': classificacoes,
        'grupos': grupos
    })


def editar_rota(request):
    # Esta função simplesmente renderiza o template editar_rota.html sem dados adicionais
    return render(request, 'distribuicao/editar_rota.html')


def configurar_distribuicao(request):
    # Renderizando com o caminho do app
    return render(request, 'distribuicao/configurar_distribuicao.html')
