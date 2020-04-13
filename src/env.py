NUMERO_DE_NOS_CAMADA_ENTRADA = 63
NUMERO_DE_CAMADAS_ESCONDIDAS = 1
NUMERO_DE_NOS_CAMADA_ESCONDIDA = 6
NUMERO_DE_NOS_CAMADA_SAIDA = 7

TAXA_DE_APRENDIZADO = 0.7
BIAS = 1
NUMERO_DE_EPOCAS = 100

ARQUIVO_DE_LEITURA = 'Part-1/caracteres-limpos.csv'
RESPOSTAS_ARQUIVO_DE_LEITURA = {
    'A': [1, -1, -1, -1, -1, -1, -1],
    'B': [-1, 1, -1, -1, -1, -1, -1],
    'C': [-1, -1, 1, -1, -1, -1, -1],
    'D': [-1, -1, -1, 1, -1, -1, -1],
    'E': [-1, -1, -1, -1, 1, -1, -1],
    'J': [-1, -1, -1, -1, -1, 1, -1],
    'K': [-1, -1, -1, -1, -1, -1, 1]
}

def divir_taxa_aprendizado(epoca):
    taxa_de_aprendizado = TAXA_DE_APRENDIZADO / (epoca+0.5)
    return taxa_de_aprendizado