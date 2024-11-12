from django.shortcuts import render

def estatisticas(request):
    from django.template.loader import render_to_string
    
    columns = ["Atendente", "Unidade", "Em Análise", "C/ Pendências", "Concluído", "Devolvido", "Cancelado", "Total", "Ações"]
    table_data = []
    
    atendentes = [
        {
            'nome': 'BENEDETABUENO',
            'unidade': 'FÁCIL BOM CLIMA TARDE',
            'em_analise': 62,
            'pendencias': 8,
            'concluido': 28,
            'devolvido': 9,
            'cancelado': 0,
            'total': 107
        },
        {
            'nome': 'MARIASILVA',
            'unidade': 'FÁCIL BOM CLIMA MANHÃ',
            'em_analise': 45,
            'pendencias': 12,
            'concluido': 32,
            'devolvido': 5,
            'cancelado': 2,
            'total': 96
        },
        {
            'nome': 'JOAOSANTOS',
            'unidade': 'FÁCIL BONSUCESSO',
            'em_analise': 38,
            'pendencias': 15,
            'concluido': 25,
            'devolvido': 7,
            'cancelado': 1,
            'total': 86
        }
    ]

    for a in atendentes:
        row = [
            f'<div class="text-center">{a["nome"]}</div>',
            f'<div class="text-center">{a["unidade"]}</div>',
            f'<div class="text-center">{a["em_analise"]}</div>',
            f'<div class="text-center">{a["pendencias"]}</div>',
            f'<div class="text-center">{a["concluido"]}</div>',
            f'<div class="text-center">{a["devolvido"]}</div>',
            f'<div class="text-center">{a["cancelado"]}</div>',
            f'<div class="text-center">{a["total"]}</div>',
            f'''<div class="text-center">
                <button class="br-button circle small" type="button" title="Imprimir">
                    <i class="fas fa-print text-primary" aria-hidden="true"></i>
                </button>
                <button class="br-button circle small" type="button" title="Salvar">
                    <i class="fas fa-save text-success" aria-hidden="true"></i>
                </button>
            </div>'''
        ]
        table_data.append(row)

    context = {
        'title': 'Resumo por Atendente',
        'columns': columns,
        'table_data': table_data,
        'grid_id': 'atendentes'
    }
    
    grid = render_to_string('components/ggrid.html', context)
    
    return render(request, 'relatorios/estatisticas.html', {'grid': grid})
