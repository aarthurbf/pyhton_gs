# Simulação de coleta de dados por drones submarinos
def coletar_dados():
    # Dados coletados em 10 pontos diferentes
    dados = [
        {'temperatura': 25.5, 'salinidade': 35.0, 'ph': 8.0, 'poluicao': 10.0},
        {'temperatura': 26.0, 'salinidade': 36.0, 'ph': 8.1, 'poluicao': 12.0},
        {'temperatura': 24.5, 'salinidade': 34.5, 'ph': 8.2, 'poluicao': 9.0},
        {'temperatura': 23.0, 'salinidade': 35.5, 'ph': 8.3, 'poluicao': 11.0},
        {'temperatura': 27.0, 'salinidade': 37.0, 'ph': 7.9, 'poluicao': 8.0},
        {'temperatura': 22.5, 'salinidade': 33.0, 'ph': 8.4, 'poluicao': 15.0},
        {'temperatura': 25.0, 'salinidade': 36.5, 'ph': 8.0, 'poluicao': 10.5},
        {'temperatura': 24.0, 'salinidade': 35.0, 'ph': 8.1, 'poluicao': 7.0},
        {'temperatura': 26.5, 'salinidade': 37.5, 'ph': 7.8, 'poluicao': 9.5},
        {'temperatura': 23.5, 'salinidade': 34.0, 'ph': 8.2, 'poluicao': 12.5}
    ]
    return dados

# Análise dos dados coletados
def analisar_dados(dados):
    temperatura_total = 0
    salinidade_total = 0
    ph_total = 0
    poluicao_total = 0

    for dado in dados:
        temperatura_total += dado['temperatura']
        salinidade_total += dado['salinidade']
        ph_total += dado['ph']
        poluicao_total += dado['poluicao']

    # Cálculo da média dos parâmetros
    temperatura_media = temperatura_total / len(dados)
    salinidade_media = salinidade_total / len(dados)
    ph_medio = ph_total / len(dados)
    poluicao_media = poluicao_total / len(dados)

    analise = {
        'temperatura_media': temperatura_media,
        'salinidade_media': salinidade_media,
        'ph_medio': ph_medio,
        'poluicao_media': poluicao_media
    }

    return analise

# Função para classificar a qualidade dos parâmetros
def classificar_parametros(analise):
    def classificar(valor, bom_limite, medio_limite):
        if valor <= bom_limite:
            return 'Boa'
        elif valor <= medio_limite:
            return 'Média'
        else:
            return 'Alta'

    classificacao = {
        'temperatura': classificar(analise['temperatura_media'], 25.0, 26.5),
        'salinidade': classificar(analise['salinidade_media'], 35.0, 37.0),
        'ph': classificar(analise['ph_medio'], 8.0, 8.3),
        'poluicao': classificar(analise['poluicao_media'], 10.0, 12.0)
    }

    return classificacao

# Geração de relatório
def gerar_relatorio(analise, classificacao):
    relatorio = (
        f"Relatório de Dados Ambientais dos Oceanos\n"
        f"-------------------------------------------\n"
        f"Temperatura Média: {analise['temperatura_media']:.2f} °C - {classificacao['temperatura']}\n"
        f"Salinidade Média: {analise['salinidade_media']:.2f} PSU - {classificacao['salinidade']}\n"
        f"pH Médio: {analise['ph_medio']:.2f} - {classificacao['ph']}\n"
        f"Nível Médio de Poluição: {analise['poluicao_media']:.2f} ppm - {classificacao['poluicao']}\n"
    )
    return relatorio

# Função principal para executar o protótipo
def main():
    dados = coletar_dados()
    analise = analisar_dados(dados)
    classificacao = classificar_parametros(analise)
    relatorio = gerar_relatorio(analise, classificacao)
    print(relatorio)

# Execução do protótipo
main()
