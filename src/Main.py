import csv
import logging
import sys
import time

from src.env import NUMERO_DE_EPOCAS, divir_taxa_aprendizado, NUMERO_DE_CAMADAS_ESCONDIDAS, \
    NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_NOS_CAMADA_SAIDA, BIAS
from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural


inputs = Mapper().arquivo
rede_neural = RedeNeural()
for epoca in range(NUMERO_DE_EPOCAS):
    for input in inputs:
        rede_neural.treinar(input['i'], input['valor'])

log_file = open('../logs/Log - ' + time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")

for input in inputs:
    rede_neural.camada_entrada = input['valor']

    rede_neural.feedforward()

    log_file.write('\n')
    log_file.write('Letra ' + input['i'] + '\n')
    logging.info('Camada de saída:')
    for perceptron in rede_neural.camada_saida:
        log_file.write(str(perceptron.saida) + "\n")
