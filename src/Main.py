"""
    Classe responsavel por controlar toda a execução do algoritmo Multilayer Perceptron, tanto para sua fase de
    treinamento, quanto para sua fase de teste
"""

import time
from src.env import NUMERO_DE_EPOCAS, TAXA_DE_APRENDIZADO, NUMERO_DE_CAMADAS_ESCONDIDAS
from src.helpers.Mapper import Mapper
from src.helpers.Logger import Logger
from src.structures.RedeNeural import RedeNeural


def inicializa_rede(file):
    num_nos_camada_entrada = len(file['inputs'][0]['sample'])
    num_camadas_escondidas = NUMERO_DE_CAMADAS_ESCONDIDAS
    """
         O numero de nos na camada escondida e calculado como sendo a metade do numero de entradas, assim, 
         independente do problema, automaticamente se pode estabelecer esse parametro

    """
    num_nos_camada_escondida = int(len(file['inputs'][0]['sample']) / 2)
    num_nos_camada_saida = len(file['inputs'][0]['target_value'])

    """
        Para cada problema, uma rede eh instanciada de acordo com seus respectivos parametros
    """
    rede_neural = RedeNeural(TAXA_DE_APRENDIZADO,
                             num_nos_camada_entrada,
                             num_camadas_escondidas,
                             num_nos_camada_escondida,
                             num_nos_camada_saida)

    return rede_neural


def treinar_rede(rede_neural, file, logger):
    """
        Para testarmos o problema dos caracteres com ruido, iremos fazer a aplicacao dele na rede que foi
        treinada pelo problema dos caracteres limpos
    """
    logger.log_inputs(rede_neural, file)
    logger.log_line(f'Numero de epocas: {NUMERO_DE_EPOCAS}')
    logger.log_line()
    for input in file['inputs']:
        logger.log_weights(rede_neural)

        rede_neural.treinar(NUMERO_DE_EPOCAS, input['target_value'], input['sample'], input['target'], logger)

        logger.log_weights(rede_neural)


def testar_rede(rede_neural, file, logger):
    logger.log_inputs(rede_neural, file)
    logger.log_line()
    for input in file['inputs']:
        rede_neural.testar(input['sample'], input['target'], logger)


def main():
    mapper = Mapper()
    train_files = mapper.arquivos_treino
    test_files = mapper.arquivos_teste

    """
        Para cada problema mapeado, iremos realizar o treino abaixo, onde cada amostra do problema em questao passa 
        pela rede neural e gera logs de seus resultados
    """
    for file in train_files:
        rede_neural = inicializa_rede(file)
        logger = Logger(file)
        treinar_rede(rede_neural, file, logger)
        logger.end_logger()

    for file in test_files:
        logger = Logger(file, True)
        testar_rede(rede_neural, file, logger)
        logger.end_logger()


if __name__ == '__main__':
    main()
