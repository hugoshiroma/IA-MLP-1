from numpy import random


class Rede:
    def __init__(self, camada_entrada, tam_camada_escondida, tam_camada_saida, num_epocas):
        self.a = random.random()
        self.camada_entrada = camada_entrada
        self.tam_camada_escondida = tam_camada_escondida
        self.tam_camada_saida = tam_camada_saida
        self.num_epocas = num_epocas

    # por enquanto estou considerando que sempre será mandado uma lista onde o último item é a resposta esperada
    def treinar(self):
        # basicamente é aqui que vai ficar o algoritmo do MPL
        caracteres = self.camada_entrada
        # coloquei nomes específicos ao nosso problema, mas podemos mudar pra nomes mais genéricos dps

        # para cada par de treinamento s: t
        for caracter in caracteres:
            target = caracter[-1] #t
            entradas = caracter[:-1] #s

            bias = random.random()
            matriz_pesos = [] # a matriz aqui será uma lista de listas
            for x in range(len(entradas)):
                pesos = []
                for neuronio_escondido in range(self.tam_camada_escondida):
                    pesos.append(random.random())
                matriz_pesos.append(pesos)
                # na linha acima, colocamos os pesos para cada entrada x em relacao ao neuronio i da cama_escondida

            print("Taxa de aprendizado da rede:", self.a)
            print("Target:", target)
            print("Bias:", bias)
            print("Matriz de pesos:")
            i = 1
            for pesos in matriz_pesos:
                print(i, pesos)
                i += 1
            print()

            self.feedforward()
            self.backpropagation()
            self.ajustar_pesos()

        # aqui imagino que o treinar devera retornar o valor dos pesos, o treinamento é feito nessa função

    def feedforward(self):
        return

    def backpropagation(self):
        return

    def ajustar_pesos(self):
        return




