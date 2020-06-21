"""
    Este eh o arquivo environment, responsavel por deter todas os valores configuraveis que definem as caracteristicas
    de funcionamento da rede neural.
"""

"""
    Estas sao as taxas que sao utilizadas para treino da rede.
"""
TAXA_DE_APRENDIZADO = 0.6
BIAS = 1
NUMERO_DE_EPOCAS = 100
NUMERO_DE_CAMADAS_ESCONDIDAS = 1


"""
    Estes sao os nomes dos arquivos que sao utilizados para treino da rede. Para funcionamento correto, eh necessario que os
    arquivos nomeados abaixo estejam todos de fato dentro da pasta '/inputs'.
"""
ARQUIVOS_PARA_TREINO = ['problemAND.csv', 'problemOR.csv', 'problemXOR.csv', 'caracteres-limpos.csv']


"""
    Estes sao os nomes dos arquivos que sao utilizados para teste da rede. Para funcionamento correto, eh necessario que os
    arquivos nomeados abaixo estejam todos de fato dentro da pasta '/inputs/Part-1'.
"""
ARQUIVOS_PARA_TESTE = ['caracteres-ruidos.csv']


"""
    Estes sao os valores de targets esperados como saida da rede para cada arquivo utilizado no treino e teste da mesma. 
"""
TARGETS = {
    'problemAND.csv': {
        '0': [0],
        '1': [1]
    },
    'problemOR.csv': {
        '0': [0],
        '1': [1]
    },
    'problemXOR.csv': {
        '0': [0],
        '1': [1]
    },
    'caracteres-limpos.csv': {
        'A': [1, -1, -1, -1, -1, -1, -1],
        'B': [-1, 1, -1, -1, -1, -1, -1],
        'C': [-1, -1, 1, -1, -1, -1, -1],
        'D': [-1, -1, -1, 1, -1, -1, -1],
        'E': [-1, -1, -1, -1, 1, -1, -1],
        'J': [-1, -1, -1, -1, -1, 1, -1],
        'K': [-1, -1, -1, -1, -1, -1, 1]
    },
    'caracteres-ruidos.csv': {
        'A': [1, -1, -1, -1, -1, -1, -1],
        'B': [-1, 1, -1, -1, -1, -1, -1],
        'C': [-1, -1, 1, -1, -1, -1, -1],
        'D': [-1, -1, -1, 1, -1, -1, -1],
        'E': [-1, -1, -1, -1, 1, -1, -1],
        'J': [-1, -1, -1, -1, -1, 1, -1],
        'K': [-1, -1, -1, -1, -1, -1, 1]
    }
}

