from random import random
import numpy as np


class Rede(object):
    def __init__(self, sizes):
        self.num_camadas = len(sizes)
        self

    def feedforward(self):
        return

    def backpropagation(self):
        return

    def ajustar_pesos(self):
        return

    # por enquanto estou considerando que sempre será mandado uma lista onde o último item é a resposta esperada
    def treinar(dado):
        # basicamente é aqui que vai ficar o algoritmo do MPL

        target = dado[-1]
        entradas = dado[:-1]

        # taxa de aprendizado
        a = random()
        bias = 1
        camada_escondida = [1, 2, 3]
        # ainda não entendi qual será o tamanho dessa lista, coloquei 3 elementos só pra testar

        for x in entradas:
            # estabelecendo pesos para essa entrada
            # a qtd de pesos será a qtd de neurônios que existem na camada escondida
            pesos = []
            for neuronio_escondido in camada_escondida:
                pesos.append(random())
            print(a, target, len(pesos), pesos)

        #print(a, target, entradas)
        feedforward()
        backpropagation()
        ajustar_pesos()

        # aqui imagino que o treinar devera retornar o valor dos pesos, o treinamento é feito nessa função



