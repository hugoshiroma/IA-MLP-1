import time

from src.structures.Perceptron import Perceptron


class RedeNeural:
    def __init__(self, taxa_aprendizado, num_nos_camada_entrada, num_camadas_escondidas,
                 num_nos_camada_escondida, num_nos_camada_saida):
        self.target = ''
        self.problema = ''
        self.camada_entrada = []
        self.taxa_aprendizado = taxa_aprendizado
        self.num_nos_camada_entrada = num_nos_camada_entrada
        self.num_camadas_escondidas = num_camadas_escondidas
        self.num_nos_camada_escondida = num_nos_camada_escondida
        self.num_nos_camada_saida = num_nos_camada_saida
        self.camadas_escondidas = self.__inicializar_camada('escondida')
        self.camada_saida = self.__inicializar_camada('saida')

    def treinar(self, epocas, target, sample, target_description):
        for epoca in range(epocas):
            self.target = target
            self.camada_entrada = sample
            self.feedforward()
            self.backpropagation(target_description)

    def feedforward(self):
        for camada in range(self.num_camadas_escondidas):
            for perceptron in range(self.num_nos_camada_escondida):
                if camada is 0:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camada_entrada)
                    self.camadas_escondidas[camada][perceptron].calcular_saida()
                else:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camadas_escondidas[camada-1])
                    self.camadas_escondidas[camada][perceptron].calcular_saida()

            if camada is self.num_camadas_escondidas-1:
                for perceptron in range(self.num_nos_camada_saida):
                    self.camada_saida[perceptron].calcular_entrada_total(self.camadas_escondidas[camada])
                    self.camada_saida[perceptron].calcular_saida()

    def backpropagation(self, target_description):
        erros = []
        correcao_pesos = []

        erros.append(self.__calcular_informacao_erro(self, self.camada_saida))
        correcao_pesos.append(self.__calcular_correcao_pesos(self, self.camada_saida, erros[0]))

        for camada in range(len(self.camadas_escondidas), -1, -1):
            if camada is not 0:
                erros.insert(0, self.__calcular_informacao_erro(self, self.camadas_escondidas[camada-1], erros[0]))
                correcao_pesos.insert(0, self.__calcular_correcao_pesos(self, self.camadas_escondidas[camada-1], erros[0]))

        log_file = open(f"../logs/{self.problema}/Log_Erros - " +
                        'Target ' + str(target_description) + time.strftime(" - %H.%M.%S - %d %m %Y.txt"), "w")
        log_file.write('CAMADA: cam_saida \n')
        for perceptron in range(len(erros[-1])):
            log_file.write('Perceptron: ' + str(perceptron + 1) + '\n')
            log_file.write(f'Erro: {erros[-1][perceptron]}' + "\n")
            log_file.write('\n')
        log_file.write('CAMADA: cam_escondida \n')
        for perceptron in range(len(erros[0])):
            log_file.write('Perceptron: ' + str(perceptron + 1) + '\n')
            log_file.write(f'Erro: {erros[0][perceptron]}' + "\n")
            log_file.write('\n')

        log_file = open(f"../logs/{self.problema}/Log_Saidas - {time.strftime('%H.%M.%S - %d %m %Y.txt')}",
                        "w")
        log_file.write('Target ' + str(target_description) + '\n')
        for perceptron in self.camada_saida:
            log_file.write(str(perceptron.saida) + "\n")
        log_file.write('\n')

        self.__ajustar_pesos(self.camada_saida, correcao_pesos[-1])
        for camada in range(len(self.camadas_escondidas), -1, -1):
            if camada is not 0:
                self.__ajustar_pesos(self.camadas_escondidas[camada-1], correcao_pesos[camada-1])

    def testar(self, target, sample, target_description):
        self.target = target
        self.camada_entrada = sample
        self.feedforward()

        log_file = open(f"../logs/testes/Log_Saidas {target_description} - {time.strftime('%H.%M.%S - %d %m %Y.txt')}",
                        "w")
        log_file.write('Target ' + str(target_description) + '\n')
        for perceptron in self.camada_saida:
            log_file.write(str(perceptron.saida) + "\n")
        log_file.write('\n')

    @staticmethod
    def __calcular_informacao_erro(self, camada, erros_entrada=[]):
        erros = []
        if camada is self.camada_saida:
            for perceptron in range(len(camada)):
                resposta_esperada = self.target[perceptron]
                info_erro = (resposta_esperada - camada[perceptron].saida) * camada[perceptron].aplicar_funcao_ativacao_derivada(camada[perceptron].entrada_total)
                erros.append(info_erro)
        elif camada is self.camadas_escondidas[-1]:
            for perceptron_escondido in range(len(camada)):
                correcao_de_peso = 0
                for perceptron_saida in range(len(self.camada_saida)):
                    correcao_de_peso += erros_entrada[perceptron_saida] * float(self.camada_saida[perceptron_saida].pesos_entrada[perceptron_escondido])
                correcao_de_peso * camada[perceptron_escondido].aplicar_funcao_ativacao_derivada(camada[perceptron_escondido].entrada_total)
                erros.append(correcao_de_peso)

            # TODO: mais um if para considerar possibilidade de mais camadas

        return erros

    @staticmethod
    def __calcular_correcao_pesos(self, camada, erros):
        correcao_de_pesos = []
        if camada is self.camada_saida:
            for perceptron_escondido in self.camadas_escondidas[-1]:
                correcao_de_pesos_perceptron_iterando = []
                for perceptron_saida in range(len(camada)):
                    correcao_de_peso = self.taxa_aprendizado * float(erros[perceptron_saida]) * float(perceptron_escondido.saida)
                    correcao_de_pesos_perceptron_iterando.append(correcao_de_peso)
                correcao_de_pesos.append(correcao_de_pesos_perceptron_iterando)
        elif camada is self.camadas_escondidas[-1]:
            for entrada in self.camada_entrada:
                correcao_de_pesos_perceptron_iterando = []
                for perceptron_escondido in range(len(camada)):
                    correcao_de_peso = self.taxa_aprendizado * float(erros[perceptron_escondido]) * float(entrada)
                    correcao_de_pesos_perceptron_iterando.append(correcao_de_peso)
                correcao_de_pesos.append(correcao_de_pesos_perceptron_iterando)
        return correcao_de_pesos

    # @staticmethod
    # def __calcular_correcao_bias(camada, erros):
    #     correcao_de_bias = []
    #     for perceptron in range(len(camada)):
    #         correcao_de_bias = self.taxa_aprendizado * erros[perceptron]
    #         correcao_de_bias.append(correcao_de_bias)
    #     return correcao_de_bias

    def __ajustar_pesos(self, camada, correcao_pesos):
        if camada is self.camada_saida:
            for perceptron in camada:
                for peso in range(len(perceptron.pesos_entrada)):
                    novo_peso = float(perceptron.pesos_entrada[peso]) + float(correcao_pesos[peso][camada.index(perceptron)])
                    perceptron.pesos_entrada[peso] = novo_peso
        else:
            for perceptron in camada:
                for peso in range(len(perceptron.pesos_entrada)):
                    novo_peso = float(perceptron.pesos_entrada[peso]) + float(correcao_pesos[peso][camada.index(perceptron)])
                    perceptron.pesos_entrada[peso] = novo_peso

    # TODO: (Bel) deixei o método não estático pra poder utilizar outros atributos dessa classe
    def __inicializar_camada(self, camada):
        if camada is 'escondida':
            camada_escondida = []
            for camada in range(self.num_camadas_escondidas):
                camada_escondida_temp = []
                if camada is 0:
                    for perceptron in range(self.num_nos_camada_escondida):
                        camada_escondida_temp.append(Perceptron(self.num_nos_camada_entrada))
                    camada_escondida.append(camada_escondida_temp)
                else:
                    for perceptron in range(self.num_nos_camada_escondida):
                        camada_escondida_temp.append(Perceptron(self.num_nos_camada_escondida))
                    camada_escondida.append(camada_escondida_temp)
            return camada_escondida

        elif camada is 'saida':
            camada_saida = []
            for perceptron in range(self.num_nos_camada_saida):
                camada_saida.append(Perceptron(self.num_nos_camada_escondida))
            return camada_saida
