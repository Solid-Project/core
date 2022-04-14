# SOLID
## Core Project

## Use Cases

 - Como investidor desejo:
    1. conta:
        - me cadastrar na plataforma
        - congelar minha conta
        - excluir minha conta
    2. portfolio:
        - adicionar diferentes investimentos
        - remover um investimento de forma personalizada
        - ver o rendimento do portfolio (porcentagem e gráfico)
        - ver o rendimento de um investimento do portfolio de forma fácil (sem precisar abri-lo)
    3. investimento:
        - adicionar transações de entrada/saída para cada investimento cadastrado
        - remover um investimento
        - adicionar um investimento a partir de um ativo
    4. ativo (product):
        - visualizar a lista de ativos disponíveis
        - pesquisar por um ativo pelo seu nome ou empresa
        - criar um ativo ainda não disponível na plataforma (preenchendo todas as especificidades necessárias)
    5. carteira:
        - criar portfolio dentro da carteira
        - remover um portfolio inteiro da carteira (deve ter operação de desfazer)
        - ver rendimento da carteira (todos os portfolios)
        - ver o rendimento unido de um ou mais portfolios
