from src.env import NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_CAMADAS_ESCONDIDAS, NUMERO_DE_NOS_CAMADA_SAIDA, \
    NUMERO_DE_EPOCAS
from src.structures.Perceptron import Perceptron


class RedeNeural:
    def __init__(self):
        self.target = ''
        self.camada_entrada = []
        self.camadas_escondidas = self.__inicializar_camada('escondida')
        self.camada_saida = self.__inicializar_camada('saida')

    def feed_forward(self, letra, valor_entrada):
        self.target = letra
        self.camada_entrada = valor_entrada

        for camada in range(NUMERO_DE_CAMADAS_ESCONDIDAS):
            for perceptron in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                if camada is 0:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camada_entrada)
                    self.camadas_escondidas[camada][perceptron].calcular_saida()
                else:
                    self.camadas_escondidas[camada][perceptron].calcular_entrada_total(self.camadas_escondidas[camada-1])
                    self.camadas_escondidas[camada][perceptron].calcular_saida()

            if camada is NUMERO_DE_CAMADAS_ESCONDIDAS:
                for perceptron in range(NUMERO_DE_NOS_CAMADA_SAIDA):
                    self.camada_saida[perceptron].calcular_entrada_total(self.camadas_escondidas[camada])

        print(self.camada_saida)

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
