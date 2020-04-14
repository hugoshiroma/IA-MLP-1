import time

NUMERO_DE_NOS_CAMADA_ENTRADA = 63
NUMERO_DE_CAMADAS_ESCONDIDAS = 1
NUMERO_DE_NOS_CAMADA_ESCONDIDA = 40
NUMERO_DE_NOS_CAMADA_SAIDA = 7

TAXA_DE_APRENDIZADO = 0.7
BIAS = 1.5
NUMERO_DE_EPOCAS = 100

DIRETORIO_DE_LOGS = ''
DIRETORIO_DE_LEITURA = 'Part-1'
ARQUIVO_DE_LEITURA = 'caracteres-limpos.csv'
ARQUIVO_DE_LEITURA_COMPLETO = DIRETORIO_DE_LEITURA + '/' + ARQUIVO_DE_LEITURA
RESPOSTAS_ARQUIVO_DE_LEITURA = {
    'A': [1, -1, -1, -1, -1, -1, -1],
    'B': [-1, 1, -1, -1, -1, -1, -1],
    'C': [-1, -1, 1, -1, -1, -1, -1],
    'D': [-1, -1, -1, 1, -1, -1, -1],
    'E': [-1, -1, -1, -1, 1, -1, -1],
    'J': [-1, -1, -1, -1, -1, 1, -1],
    'K': [-1, -1, -1, -1, -1, -1, 1]
}