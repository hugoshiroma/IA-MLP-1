import os
import time

from src.env import NUMERO_DE_EPOCAS, NUMERO_DE_NOS_CAMADA_ENTRADA, \
    NUMERO_DE_CAMADAS_ESCONDIDAS, NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_NOS_CAMADA_SAIDA, TAXA_DE_APRENDIZADO, \
    ARQUIVO_DE_LEITURA
from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural

valores_nos = [2, 5, 10, 15, 20, 30, 40, 50]
valores_aprendizado = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
valores_epocas = [5, 10, 25, 50, 100, 200, 300, 400, 500, 1000]

inputs = Mapper().arquivo
rede_neural = RedeNeural()

for qtd_no in valores_nos:
    NUMERO_DE_NOS_CAMADA_ESCONDIDA = qtd_no
    nome_diretorio_nos = '../logs/' + str(qtd_no) + ' nos na escondida'
    os.mkdir(nome_diretorio_nos)
    for taxa_aprendizado in valores_aprendizado:
        TAXA_DE_APRENDIZADO = taxa_aprendizado
        nome_diretorio_taxas = nome_diretorio_nos + '/' + 'taxa de aprendizado ' + str(taxa_aprendizado)
        os.mkdir(nome_diretorio_taxas)
        for qtd_epoca in valores_epocas:
            NUMERO_DE_EPOCAS = qtd_epoca
            nome_diretorio_epocas = nome_diretorio_taxas + '/' + str(qtd_epoca) + ' epocas'
            os.mkdir(nome_diretorio_epocas)

            log_file = open(nome_diretorio_epocas + '/Log_PesosIniciais_cam_escondida - ' +
                time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")
            log_file.write('CAMADA: cam_escondida \n')
            for perceptron in rede_neural.camadas_escondidas[0]:
                log_file.write('Perceptron: ' + str(rede_neural.camadas_escondidas[0].index(perceptron)+1) + '\n')
                for peso in perceptron.pesos_entrada:
                    log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
                log_file.write('\n')
            log_file.write('CAMADA: cam_saida \n')
            for perceptron in rede_neural.camada_saida:
                log_file.write('Perceptron: ' + str(rede_neural.camada_saida.index(perceptron)+1) + '\n')
                for peso in perceptron.pesos_entrada:
                    log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
                log_file.write('\n')

            for epoca in range(NUMERO_DE_EPOCAS):
                for input in inputs:
                    rede_neural.treinar(input['i'], input['valor'])

            log_file = open(nome_diretorio_epocas + '/Log_Parametros - ' + time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")
            log_file.write('Arquivo de leitura: ' + ARQUIVO_DE_LEITURA + '\n')
            log_file.write(f'Quantidade de nos de entrada: {NUMERO_DE_NOS_CAMADA_ENTRADA}' + '\n')
            log_file.write(f'Quantidade de camadas escondidas: {NUMERO_DE_CAMADAS_ESCONDIDAS} ' + '\n')
            log_file.write(f'Quantidade de Perceptrons nas camadas escondidas: {NUMERO_DE_NOS_CAMADA_ESCONDIDA} ' + '\n')
            log_file.write(f'Quantidade de nos de saida: {NUMERO_DE_NOS_CAMADA_SAIDA} ' + '\n')
            log_file.write(f'Taxa de aprendizado: {TAXA_DE_APRENDIZADO} ' + '\n')
            log_file.write(f'Numero de epocas: {NUMERO_DE_EPOCAS} ' + '\n')

            log_file = open(nome_diretorio_epocas + '/Log_PesosFinais_cam_escondida - ' +
                time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")
            log_file.write('CAMADA: cam_escondida \n')
            for perceptron in rede_neural.camadas_escondidas[0]:
                log_file.write('Perceptron: ' + str(rede_neural.camadas_escondidas[0].index(perceptron)+1) + '\n')
                for peso in perceptron.pesos_entrada:
                    log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
                log_file.write('\n')
            log_file.write('\n')
            log_file.write('\n')
            log_file.write('CAMADA: cam_saida \n')
            for perceptron in rede_neural.camada_saida:
                log_file.write('Perceptron: ' + str(rede_neural.camada_saida.index(perceptron)+1) + '\n')
                for peso in perceptron.pesos_entrada:
                    log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
                log_file.write('\n')


            log_file = open(nome_diretorio_epocas + '/Log_Saidas - ' + time.strftime("%H.%M.%S - %d %m %Y.txt"), "w")
            for input in inputs:
                rede_neural.camada_entrada = input['valor']
                rede_neural.feedforward()
                log_file.write('Target ' + input['i'] + '\n')
                for perceptron in rede_neural.camada_saida:
                    log_file.write(str(perceptron.saida) + "\n")
                log_file.write('\n')
