import csv
import logging

from src.env import NUMERO_DE_EPOCAS, divir_taxa_aprendizado, NUMERO_DE_CAMADAS_ESCONDIDAS, \
    NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_NOS_CAMADA_SAIDA, BIAS
from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural


inputs = Mapper().arquivo
rede_neural = RedeNeural()
for epoca in range(NUMERO_DE_EPOCAS):
    for input in inputs:
        rede_neural.treinar(input['i'], input['valor'])

for input in inputs:
    rede_neural.camada_entrada = input['valor']
    rede_neural.camada_entrada.append(BIAS)

    rede_neural.feedforward()

    logging.basicConfig(filename='../logs/pesos_treinados.txt', level=logging.INFO)
    logging.info('Letra ' + input['i'])
    logging.info('Camada de saída:')
    for perceptron in rede_neural.camada_saida:
        logging.info(perceptron.saida)
    logging.info('')
