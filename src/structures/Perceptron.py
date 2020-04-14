import random

from src.env import NUMERO_DE_NOS_CAMADA_ENTRADA, NUMERO_DE_NOS_CAMADA_ESCONDIDA
from src.env import TAXA_DE_APRENDIZADO
from src.env import BIAS
import numpy as np


class Perceptron:
    def __init__(self, camada):
        self.entrada = 0
        self.entrada_total = 0
        self.pesos_entrada = self.__inicializar_pesos(camada)
        self.saida = 0

    def calcular_entrada_total(self, entradas):
        entrada_total = 0
        if not isinstance(entradas[0], Perceptron):
            for entrada in range(len(entradas)):
                entrada_total += float(entradas[entrada]) * self.pesos_entrada[entrada]
        else:
            for entrada in range(len(entradas)):
                entrada_total += entradas[entrada].saida * self.pesos_entrada[entrada]
        self.entrada_total = entrada_total

    def calcular_saida(self):
        self.saida = self.aplicar_funcao_ativacao(self.entrada_total)

    @staticmethod
    def aplicar_funcao_ativacao(valor):
        return 1 / (1 + np.exp(-valor))

    def aplicar_funcao_ativacao_derivada(self, valor):
        return self.aplicar_funcao_ativacao(valor) * (1 - self.aplicar_funcao_ativacao(valor))

    @staticmethod
    def __inicializar_pesos(camada):
        pesos = []

        if camada is 'cam_entrada':
            for i in range(NUMERO_DE_NOS_CAMADA_ENTRADA):
                pesos.append(random.randrange(-1, 2))
            return pesos

        if camada is 'cam_escondida' or 'cam_saida':
            for i in range(NUMERO_DE_NOS_CAMADA_ESCONDIDA):
                pesos.append(random.randrange(-1, 2))
            return pesos

    def __ajustar_pesos(self):
        return
