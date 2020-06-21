"""
    Classe responsavel por fazer os logs dos parametros utilizados na inicializacao da rede e posteriormente em seu
    treinamento e teste por cada problema distinto.

    Functions:

"""

import time


class Logger:
    def __init__(self, file, is_test=False):
        if is_test is True:
            self.logfile_path = f"../logs/testes/{file['filename']}/Logfile - " \
                                f"{time.strftime('%H.%M.%S - %d-%m-%Y.txt')}"
        else:
            self.logfile_path = f"../logs/{file['filename']}/Logfile - " \
                                f"{time.strftime('%H.%M.%S - %d-%m-%Y.txt')}"
        self.logfile = open(self.logfile_path, 'w')

    def log_inputs(self, rede_neural, file):
        self.log_line(f"Arquivo lido: {file['filename']} ")
        self.log_line(f'Quantidade de perceptrons na camada de entrada: {rede_neural.num_nos_camada_entrada} ')
        self.log_line(f'Quantidade de camadas escondidas: {rede_neural.num_camadas_escondidas} ')
        self.log_line(f'Quantidade de perceptrons na(s) camada(s) escondida(s): {rede_neural.num_nos_camada_escondida} ')
        self.log_line(f'Quantidade de perceptrons na camada de saida: {rede_neural.num_nos_camada_saida} ')
        self.log_line(f'Taxa de aprendizado: {rede_neural.taxa_aprendizado} ')

    def log_weights(self, rede_neural):
        self.log_line('Pesos')
        for camada in range(len(rede_neural.camadas_escondidas)):
            if camada is 0:
                self.log_line(f'Camada de entrada -> camada escondida[{camada}]')
            else:
                self.log_line(f'Camada escondida[{camada-1}] -> camada escondida[{camada}]')
            for perceptron in rede_neural.camadas_escondidas[camada]:
                self.log_line(f'Perceptron {str(rede_neural.camadas_escondidas[camada].index(perceptron) + 1)}')
                for peso in perceptron.pesos_entrada:
                    self.log_line(f'Peso {perceptron.pesos_entrada.index(peso) + 1}: {peso}')
                self.log_line()
        self.log_line(f'Camada escondida[{rede_neural.camadas_escondidas.index(rede_neural.camadas_escondidas[-1])}] -> camada de saida')
        for perceptron in rede_neural.camada_saida:
            self.log_line(f'Perceptron {str(rede_neural.camada_saida.index(perceptron) + 1)}')
            for peso in perceptron.pesos_entrada:
                self.log_line(f'Peso {perceptron.pesos_entrada.index(peso) + 1}: {peso}')
            self.log_line()
        
    def log_outputs(self, rede_neural, target, erros, epoca):
        self.log_line(f'Epoca {epoca + 1}')
        self.log_line('Output')
        for camada in erros:
            if camada is not erros[-1]:
                self.log_line(f'Camada escondida[{erros.index(camada)}]')
                for perceptron in range(len(camada)):
                    self.log_line(f'Perceptron {str(perceptron + 1)}')
                    self.log_line(f'Erro: {camada[perceptron]}')
                self.log_line()
            else:
                self.log_line('Camada de saida')
                for perceptron in range(len(camada)):
                    self.log_line(f'Perceptron {str(perceptron + 1)}')
                    self.log_line(f'Erro: {erros[-1][perceptron]}')
                self.log_line()

        self.log_line(f'Saida para target {str(target)}')
        for perceptron in rede_neural.camada_saida:
            self.log_line(f'Perceptron {str(rede_neural.camada_saida.index(perceptron))}')
            self.log_line(f'Saida: {str(perceptron.saida)}')
        self.log_line()

    def log_line(self, line=''):
        self.logfile.write(f'{line}\n')

    def end_logger(self):
        self.logfile.close()
