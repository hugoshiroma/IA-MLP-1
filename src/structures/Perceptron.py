import random
import numpy as np


class Perceptron:
    def __init__(self, num_nos_conectados):
        self.entrada = 0
        self.entrada_total = 0
        self.num_nos_conectados = num_nos_conectados
        self.pesos_entrada = self.__inicializar_pesos()
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

    # TODO: (Bel) deixei o método não estático pra poder utilizar outros atributos dessa classe.
    #  Tirei o if porque na Rede Neural a gente já envia a quantidade de nos que esse Perceptron
    #  está conectado para poder inicializar a matriz de pesos
    def __inicializar_pesos(self):
        pesos = []
        for i in range(self.num_nos_conectados):
            pesos.append(random.randrange(-1, 2))
        return pesos

    def __ajustar_pesos(self):
        return
