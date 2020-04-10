from src.env import NUMERO_DE_NOS_CAMADA_ENTRADA, NUMERO_DE_NOS_CAMADA_ESCONDIDA
from src.env import TAXA_DE_APRENDIZADO
from src.env import BIAS
import numpy as np


class Perceptron:
    def __init__(self, camada):
        self.entrada_total = 0
        self.pesos_entrada = self.__inicializar_pesos(camada)
        self.saida = 0

    def calcular_entrada_total(self, entradas):
        entrada_total = 0
        for entrada in entradas:
            if not isinstance(entrada, Perceptron):
                entrada_total += float(entrada) * self.pesos_entrada[entradas.index(entrada)]
                entrada_total = entrada_total + BIAS
            else:
                entrada_total += entrada.saida * self.pesos_entrada[entradas.index(entrada)]
        self.entrada_total = entrada_total

    def calcular_saida(self):
        self.saida = self.__aplicar_funcao_ativacao(self.entrada_total)

    @staticmethod
    def __aplicar_funcao_ativacao(valor):
        return 1 / (1 + np.exp((-TAXA_DE_APRENDIZADO) * valor))

    @staticmethod
    def aplicar_funcao_ativacao_derivada(valor):
        return np.exp(-valor) / ((1 + np.exp(-valor))**2)

    @staticmethod
    def __inicializar_pesos(camada):
        pesos = []

        if camada is 'cam_entrada':
            for i in range(NUMERO_DE_NOS_CAMADA_ENTRADA):
                pesos.append(np.random.uniform(low=-1, high=1))
            return pesos

        if camada is 'cam_escondida' or 'cam_saida':
            for i in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                pesos.append(np.random.random())
            return pesos

    def __ajustar_pesos(self):
        return
