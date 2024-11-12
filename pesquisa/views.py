from django.views.generic import TemplateView

class PesquisaAvancadaView(TemplateView):  # Removido o LoginRequiredMixin
    template_name = 'pesquisa/pesquisa_avancada.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Dados simulados para o grid de resultados
        dados_grid = [
            {
                'protocolo': '2024001234',
                'assunto': 'Licença de Funcionamento',
                'solicitante': 'João Silva',
                'cpf_cnpj': '123.456.789-00',
                'data_entrada': '15/01/2024',
                'status': 'Em Análise',
                'unidade': 'Fácil Centro',
                'classificacao': 'Licenciamento DRM VRE',
                'prioridade': True
            },
            {
                'protocolo': '2024001235',
                'assunto': 'Certidão Negativa',
                'solicitante': 'Maria Santos',
                'cpf_cnpj': '987.654.321-00',
                'data_entrada': '16/01/2024',
                'status': 'Nova',
                'unidade': 'Fácil São João',
                'classificacao': 'Certidões e Documentos',
                'prioridade': False
            },
            {
                'protocolo': '2024001236',
                'assunto': 'Alvará Sanitário',
                'solicitante': 'Empresa XYZ Ltda',
                'cpf_cnpj': '12.345.678/0001-90',
                'data_entrada': '17/01/2024',
                'status': 'Distribuída',
                'unidade': 'Fácil Pimentas',
                'classificacao': 'Meio Ambiente e VISA',
                'prioridade': True
            }
        ]

        # Criando HTML do grid com os dados simulados
        grid_html = '''
        <div class="br-table" data-search="data-search" data-selection="data-selection">
            <div class="table-header">
                <div class="top-bar">
                    <div class="table-title">Resultados da Pesquisa</div>
                </div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Protocolo</th>
                        <th>Assunto</th>
                        <th>Solicitante</th>
                        <th>CPF/CNPJ</th>
                        <th>Data Entrada</th>
                        <th>Status</th>
                        <th>Unidade</th>
                        <th>Classificação</th>
                        <th>Prioridade</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
        '''

        for dado in dados_grid:
            prioridade_icon = '<i class="fas fa-exclamation-circle text-warning"></i>' if dado['prioridade'] else ''
            grid_html += f'''
                <tr>
                    <td>{dado['protocolo']}</td>
                    <td>{dado['assunto']}</td>
                    <td>{dado['solicitante']}</td>
                    <td>{dado['cpf_cnpj']}</td>
                    <td>{dado['data_entrada']}</td>
                    <td>{dado['status']}</td>
                    <td>{dado['unidade']}</td>
                    <td>{dado['classificacao']}</td>
                    <td class="text-center">{prioridade_icon}</td>
                    <td class="text-center">
                        <button class="br-button secondary circle small" type="button" title="Visualizar">
                            <i class="fas fa-eye"></i>
                        </button>
                        <button class="br-button primary circle small" type="button" title="Editar">
                            <i class="fas fa-edit"></i>
                        </button>
                    </td>
                </tr>
            '''

        grid_html += '''
                </tbody>
            </table>
        </div>
        '''

        context['grid'] = grid_html
        return context
