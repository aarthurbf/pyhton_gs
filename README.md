# Simulação de Coleta de Dados por Drones Submarinos

### Nome e Rm: 
- Arthur Bobadilla Franchi 555056
- Igor Nascimento Medeiros 555337

## Detalhes do Projeto
Este projeto visa simular a coleta de dados ambientais dos oceanos utilizando drones submarinos. A simulação inclui a coleta de dados sobre temperatura, salinidade, pH e poluição em diferentes pontos do oceano. Em seguida, esses dados são analisados para calcular médias e classificar a qualidade dos parâmetros medidos. Um relatório é gerado com base nos resultados da análise.

## Funcionalidades
1. **Coleta de Dados**: Simula a coleta de dados em 10 pontos diferentes do oceano.

2. **Análise dos Dados**: Calcula as médias dos parâmetros coletados.

3. **Classificação dos Parâmetros**: Classifica a qualidade dos parâmetros com base em limites definidos.

4. **Geração de Relatório**: Gera um relatório detalhado com os resultados da análise e classificações.

## Instruções de Uso

#### Simulação
1. Clone o Repositório

2. Navegue até o Diretório do Projeto

3. Execute o Script

#### Caso Real
1. **Aquisição de Hardware**: Drones submarinos equipados com sensores de temperatura, salinidade, pH e poluição.

2. **Configuração de Sensores**: Calibrar os sensores antes da coleta de dados para garantir a precisão das medições.

3. **Desenvolvimento de Software**: Desenvolver um software embarcado para controlar os drones e coletar os dados dos sensores. Utilizar linguagens como Python para processamento de dados e análises.

4. **Implementação de Redes de Comunicação**: Estabelecer uma rede de comunicação entre os drones e uma base central para a transmissão dos dados coletados.

5. **Processamento de Dados**: Transferir os dados coletados dos drones para um servidor central para processamento e análise. Utilizar bibliotecas Python como Pandas e NumPy para a análise de dados.

6. **Análise e Classificação**: Implementar algoritmos para calcular médias e classificar a qualidade dos parâmetros medidos. Utilizar visualizações de dados para interpretar os resultados (por exemplo, Matplotlib).

7. **Geração de Relatórios**: Gerar relatórios detalhados e visualizações para apresentar os resultados da análise. Utilizar ferramentas de BI (Business Intelligence) para relatórios mais avançados.

## Requisitos
- Python 3.6 ou superior

- Pandas (para processamento de dados no caso real)

- NumPy (para processamento numérico no caso real)

- Matplotlib (para visualização no caso real)

## Dependências

#### Simulaçao
Este projeto de simulação não possui dependências adicionais além do Python 3 padrão.

#### Caso Real 
- **Pandas**: Biblioteca para análise de dados.

- **NumPy**: Biblioteca para computação numérica.

- **Matplotlib**: Biblioteca para visualização de dados

## Estrutura do Código
- **coletar_dados()**: Função que simula a coleta de dados em 10 pontos diferentes do oceano.

- **analisar_dados(dados)**: Função que analisa os dados coletados, calculando as médias dos parâmetros.

- **classificar_parametros(analise)**: Função que classifica a qualidade dos parâmetros com base nas médias calculadas.

- **gerar_relatorio(analise, classificacao)**: Função que gera um relatório detalhado com os resultados da análise e classificação.

- **main()**: Função principal que coordena a execução do script, chamando as funções de coleta, análise, classificação e geração de relatório.

## Exemplo de Saída
```
Relatório de Dados Ambientais dos Oceanos

Temperatura Média: 24.85 °C - Boa
Salinidade Média: 35.40 PSU - Boa
pH Médio: 8.10 - Média
Nível Médio de Poluição: 10.75 ppm - Média
```
