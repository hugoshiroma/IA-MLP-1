import time

NUMERO_DE_NOS_CAMADA_ENTRADA = 63
NUMERO_DE_CAMADAS_ESCONDIDAS = 1
NUMERO_DE_NOS_CAMADA_ESCONDIDA = 30
NUMERO_DE_NOS_CAMADA_SAIDA = 7

TAXA_DE_APRENDIZADO = 0.33
BIAS = 1
NUMERO_DE_EPOCAS = 1000

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

log_file = open('../logs/Log_Parametros - ' + time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")

log_file.write('\n')
log_file.write('ARQUIVO DE LEITURA: ' + ARQUIVO_DE_LEITURA + '\n')
log_file.write('PERCEPTRONS CAMADA DE ENTRADA: ' + NUMERO_DE_NOS_CAMADA_ENTRADA + '\n')
log_file.write('QUANTIDADE CAMADA ESCONDIDA: ' + NUMERO_DE_CAMADAS_ESCONDIDAS + '\n')
log_file.write('PERCEPTRONS CAMADA ESCONDIDA: ' + NUMERO_DE_NOS_CAMADA_ESCONDIDA + '\n')
log_file.write('PERCEPTRONS CAMADA DE SAIDA: ' + NUMERO_DE_NOS_CAMADA_SAIDA + '\n')
log_file.write('TAXA DE APRENDIZADO: ' + TAXA_DE_APRENDIZADO + '\n')
log_file.write('NUMERO DE EPOCAS: ' + NUMERO_DE_EPOCAS + '\n')

def divir_taxa_aprendizado(epoca):
    taxa_de_aprendizado = TAXA_DE_APRENDIZADO / (epoca+0.5)
    return taxa_de_aprendizado