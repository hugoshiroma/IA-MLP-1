import time
# ATENCAO: Infos da rede
TAXA_DE_APRENDIZADO = 0.5
BIAS = 1
NUMERO_DE_EPOCAS = 200

# Abaixo nomeamos os arquivos que são utilizados para treinar a rede neural
ARQUIVOS_PARA_TREINO = ['problemAND.csv', 'problemOR.csv', 'problemXOR.csv', 'caracteres-limpos.csv']
# ARQUIVOS_PARA_TREINO = ['caracteres-limpos.csv']

# Abaixo nomeamos os arquivos que são utilizados para testar a rede neural
ARQUIVOS_PARA_TESTE = ['caracteres-ruidos.csv']


def divir_taxa_aprendizado(epoca):
    taxa_de_aprendizado = TAXA_DE_APRENDIZADO / (epoca + 0.5)
    return taxa_de_aprendizado
