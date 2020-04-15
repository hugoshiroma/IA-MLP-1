"""
    Essa classe é responsável por controlar toda a execução do algoritmo Multi-layer Perceptron,
    tanto para sua fase treinamento, quanto para sua fase de teste
"""
import time
from src.env import NUMERO_DE_EPOCAS, BIAS, TAXA_DE_APRENDIZADO
from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural

problemas = Mapper().arquivos

"""
    Para cada problema mapeado, iremos realizar o treino abaixo, onde cada sample do problema em questão passa 
    pela rede neural e gera logs de seus resultados
"""

for problema in problemas:
    print(f"treinando {problema['nome_problema']}")
    num_nos_camada_entrada = len(problema['inputs'][0]['sample'])
    num_camadas_escondidas = 1
    """
         O número de nós na camada escondida é calculado como sendo a metade do numero de entradas, assim, 
         independente do problema, automaticamente se pode estabelecer esse parâmetro
         
    """
    num_nos_camada_escondida = int(len(problema['inputs'][0]['sample']) / 2)
    num_nos_camada_saida = len(problema['inputs'][0]['target'])

    """
        Para cada problema, uma rede é instanciada de acordo com seus respectivos parâmetros
    """
    rede_neural = RedeNeural(TAXA_DE_APRENDIZADO,
                             num_nos_camada_entrada,
                             num_camadas_escondidas,
                             num_nos_camada_escondida,
                             num_nos_camada_saida)

    for input in problema['inputs']:
        rede_neural.problema = problema['nome_problema']
        log_file = open(f"../logs/{problema['nome_problema']}/Log_PesosIniciais - " +
                        'Target ' + str(input['target_description']) + time.strftime(" - %H.%M.%S - %d %m %Y.txt"), "w")
        log_file.write('CAMADA: cam_escondida \n')
        for perceptron in rede_neural.camadas_escondidas[0]:
            log_file.write('Perceptron: ' + str(rede_neural.camadas_escondidas[0].index(perceptron) + 1) + '\n')
            for peso in perceptron.pesos_entrada:
                log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
            log_file.write('\n')
        log_file.write('CAMADA: cam_saida \n')
        for perceptron in rede_neural.camada_saida:
            log_file.write('Perceptron: ' + str(rede_neural.camada_saida.index(perceptron) + 1) + '\n')
            for peso in perceptron.pesos_entrada:
                log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
            log_file.write('\n')

        rede_neural.treinar(NUMERO_DE_EPOCAS, input['target'], input['sample'], input['target_description'])

        log_file.write('\n')
        log_file.write(f"Target: {input['target_description']} \n")

        log_file = open(f"../logs/{problema['nome_problema']}/Log_PesosFinais - " +
                        'Target ' + str(input['target_description']) + time.strftime(" - %H.%M.%S - %d %m %Y.txt"), "w")
        log_file.write('CAMADA: cam_escondida \n')
        for perceptron in rede_neural.camadas_escondidas[0]:
            log_file.write('Perceptron: ' + str(rede_neural.camadas_escondidas[0].index(perceptron) + 1) + '\n')
            for peso in perceptron.pesos_entrada:
                log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
            log_file.write('\n')
        log_file.write('\n')
        log_file.write('\n')
        log_file.write('CAMADA: cam_saida \n')
        for perceptron in rede_neural.camada_saida:
            log_file.write('Perceptron: ' + str(rede_neural.camada_saida.index(perceptron) + 1) + '\n')
            for peso in perceptron.pesos_entrada:
                log_file.write(f'Peso [{perceptron.pesos_entrada.index(peso)}]: {peso}' + "\n")
            log_file.write('\n')

    log_file = open(
        f"../logs/{problema['nome_problema']}/Log_Parametros_Iniciais - {time.strftime('%H.%M.%S - %d %m %Y.txt')}", "w")
    log_file.write('\n')
    log_file.write(f"ARQUIVO DE LEITURA: {problema['nome_problema']} \n")
    log_file.write(f'PERCEPTRONS CAMADA DE ENTRADA: {num_nos_camada_entrada} \n')
    log_file.write(f'QUANTIDADE CAMADA ESCONDIDA: {num_camadas_escondidas} \n')
    log_file.write(f'PERCEPTRONS CAMADA ESCONDIDA: {num_nos_camada_escondida} \n')
    log_file.write(f'PERCEPTRONS CAMADA DE SAIDA: {num_nos_camada_saida} \n')
    log_file.write(f'TAXA DE APRENDIZADO: {TAXA_DE_APRENDIZADO} \n')
    log_file.write(f'NUMERO DE EPOCAS: {NUMERO_DE_EPOCAS} \n')

    """
        Para testarmos o problema dos caracteres com ruído, iremos fazer a aplicação dele na rede que foi 
        treinada pelo problema dos caracteres limpos
    """
    if problema['nome_problema'] == 'caracteres-limpos':
        for input in Mapper().arquivos_teste[0]['inputs']:
            rede_neural.testar(input['target'], input['sample'], input['target_description'])
