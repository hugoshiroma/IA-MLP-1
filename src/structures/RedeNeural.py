from src.env import NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_CAMADAS_ESCONDIDAS, NUMERO_DE_NOS_CAMADA_SAIDA, \
    NUMERO_DE_EPOCAS, RESPOSTAS_ARQUIVO_DE_LEITURA, TAXA_DE_APRENDIZADO, BIAS
from src.structures.Perceptron import Perceptron


class RedeNeural:
    def __init__(self):
        self.target = ''
        self.camada_entrada = []
        self.taxa_aprendizado = 0
        self.camadas_escondidas = self.__inicializar_camada('escondida')
        self.camada_saida = self.__inicializar_camada('saida')

    def treinar(self, letra, valor_entrada):
        self.target = letra
        self.camada_entrada = valor_entrada

        self.feedforward()

        self.backpropagation()

    def feedforward(self):
        for camada in range(NUMERO_DE_CAMADAS_ESCONDIDAS):
            for perceptron in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                if camada is 0:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camada_entrada)
                    self.camadas_escondidas[camada][perceptron].calcular_saida()
                else:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camadas_escondidas[camada-1])
                    self.camadas_escondidas[camada][perceptron].calcular_saida()

            if camada is NUMERO_DE_CAMADAS_ESCONDIDAS-1:
                for perceptron in range(NUMERO_DE_NOS_CAMADA_SAIDA):
                    self.camada_saida[perceptron].calcular_entrada_total(self.camadas_escondidas[camada])
                    self.camada_saida[perceptron].calcular_saida()

    def backpropagation(self):
        erros = []
        correcao_pesos = []

        erros.append(self.__calcular_informacao_erro(self, self.camada_saida))
        correcao_pesos.append(self.__calcular_correcao_pesos(self, self.camada_saida, erros[0]))

        for camada in range(len(self.camadas_escondidas), -1, -1):
            if camada is not 0:
                erros.insert(0, self.__calcular_informacao_erro(self, self.camadas_escondidas[camada-1], erros[0]))
                correcao_pesos.insert(0, self.__calcular_correcao_pesos(self, self.camadas_escondidas[camada-1], erros[0]))

        # correcao_bias = self.__calcular_correcao_bias()

        self.__ajustar_pesos(self.camada_saida, correcao_pesos[-1])
        for camada in range(len(self.camadas_escondidas), -1, -1):
            self.__ajustar_pesos(self.camadas_escondidas[camada-1], correcao_pesos[camada-1])

    @staticmethod
    def __calcular_informacao_erro(self, camada, erros_entrada=[]):
        erros = []
        if camada is self.camada_saida:
            for perceptron in range(len(camada)):
                resposta_esperada = RESPOSTAS_ARQUIVO_DE_LEITURA.get(self.target)[perceptron]
                # somatorio = self.__calcular_somatorio_saidas_e_pesos(self, self.camadas_escondidas[0], perceptron)
                info_erro = (resposta_esperada - camada[perceptron].saida) * camada[perceptron].aplicar_funcao_ativacao_derivada(camada[perceptron].entrada_total)
                erros.append(info_erro)
            return erros
        else:
            for perceptron in range(len(camada)):
                soma = 0
                for erro in erros_entrada:
                    for peso in camada[perceptron].pesos_entrada:
                        soma += erro * peso
                    erro = soma * camada[perceptron].aplicar_funcao_ativacao_derivada(camada[perceptron].entrada_total)
                erros.append(erro)
            return erros

    @staticmethod
    def __calcular_somatorio_saidas_e_pesos(self, camada, perceptron_iterando):
        resp = 0
        for perceptron in range(len(self.camadas_escondidas[0])):
            resp += camada[perceptron].saida * self.camada_saida[perceptron_iterando].pesos_entrada[perceptron]
        return resp

    @staticmethod
    def __calcular_correcao_pesos(self, camada, perceptron_iterando, erros):
        correcao_de_pesos = []
        for perceptron in range(len(camada)):
            correcao_de_peso = TAXA_DE_APRENDIZADO * erros[perceptron] * float(camada[perceptron].saida)
            correcao_de_pesos.append(correcao_de_peso)
        return correcao_de_pesos

    # @staticmethod
    # def __calcular_correcao_bias(camada, erros):
    #     correcao_de_bias = []
    #     for perceptron in range(len(camada)):
    #         correcao_de_bias = TAXA_DE_APRENDIZADO * erros[perceptron]
    #         correcao_de_bias.append(correcao_de_bias)
    #     return correcao_de_bias

    def __ajustar_pesos(self, camada, correcao_pesos):
        if camada is self.camada_saida:
            for perceptron in camada:
                for peso in range(len(perceptron.pesos_entrada)):
                    novo_peso = float(perceptron.pesos_entrada[peso]) + float(correcao_pesos[camada.index(perceptron)])
                    perceptron.pesos_entrada[peso] = novo_peso
        else:
            for perceptron in camada:
                for peso in range(len(perceptron.pesos_entrada)):
                    novo_peso = float(perceptron.pesos_entrada[peso]) + float(correcao_pesos[camada.index(perceptron)])
                    perceptron.pesos_entrada[peso] = novo_peso

    @staticmethod
    def __inicializar_camada(camada):
        if camada is 'escondida':
            camada_escondida = []
            for camada in range(NUMERO_DE_CAMADAS_ESCONDIDAS):
                camada_escondida_temp = []
                if camada is 0:
                    for perceptron in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                        camada_escondida_temp.append(Perceptron('cam_entrada'))
                    camada_escondida.append(camada_escondida_temp)
                else:
                    for perceptron in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                        camada_escondida_temp.append(Perceptron('cam_escondida'))
                    camada_escondida.append(camada_escondida_temp)
            return camada_escondida

        elif camada is 'saida':
            camada_saida = []
            for perceptron in range(NUMERO_DE_NOS_CAMADA_SAIDA):
                camada_saida.append(Perceptron('cam_saida'))
            return camada_saida