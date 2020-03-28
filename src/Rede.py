import numpy as np

class Rede:
    def __init__(self, camada_entrada, tam_camada_escondida, tam_camada_saida, num_epocas, func_ativacao):
        self.a = np.random.random()
        self.camada_entrada = camada_entrada
        self.matriz_pesos = []
        self.nova_matriz_pesos = []
        self.tam_camada_escondida = tam_camada_escondida
        self.tam_camada_saida = tam_camada_saida
        self.num_epocas = num_epocas
        self.func_ativacao = func_ativacao
        self.podeIterar = False

    # por enquanto estou considerando que sempre será mandado uma lista onde o último item é a resposta esperada
    def treinar(self):
        # basicamente é aqui que vai ficar o algoritmo do MPL
        caracteres = self.camada_entrada
        # coloquei nomes específicos ao nosso problema, mas podemos mudar pra nomes mais genéricos dps

        # para cada par de treinamento s: t
        print("Caracteres:", len(caracteres))
        for caracter in caracteres:
            target = caracter[-1] #t
            entradas = caracter[:-1] #s

            bias = np.random.random()
            entradas.append(bias)
            self.criar_pesos(len(entradas), self.matriz_pesos, self.tam_camada_escondida)
            self.criar_pesos(self.tam_camada_escondida, self.nova_matriz_pesos, self.tam_camada_saida)

            # print("Taxa de aprendizado da rede:", self.a)
            # print("Target:", target)
            # print("Bias:", bias)
            # print("Matriz de pesos:")
            # i = 1
            # for pesos in matriz_pesos:
            #     print(i, pesos)
            #     i += 1
            # print()

            self.feedforward(entradas, self.matriz_pesos)
            self.backpropagation()
            self.ajustar_pesos()

        # aqui imagino que o treinar devera retornar o valor dos pesos, o treinamento é feito nessa função

    def criar_pesos(self, tam_entradas, matriz_pesos, tam_prox_camada):
        for neuronio_escondido in range(tam_prox_camada):
            pesos = []
            for x in range(tam_entradas):
                peso = np.random.random()
                pesos.append(peso)
            matriz_pesos.append(pesos)


        test = 1

            # na linha acima, colocamos os pesos para cada entrada x em relacao ao neuronio i da cama_escondida

    def feedforward(self, entradas, matriz_pesos, podeIterar = True):
        # e se for com dicts?
        camada_escondida = []
        soma = 0
        for pesos_neuronio in matriz_pesos:
            for peso in pesos_neuronio:
                soma += float(entradas[pesos_neuronio.index(peso)]) * peso
            camada_escondida.append(self.aplicar_funcao_ativacao(soma))
        # self.aplicar_funcao_ativacao(self, camada_escondida)
        if podeIterar:
            self.feedforward(camada_escondida, self.nova_matriz_pesos, False)
        else:
            camada_saida = camada_escondida
            self.calcular_deltinha(camada_escondida)
            print(camada_saida)

    def aplicar_funcao_ativacao(self, v):
        return 1/(1+np.exp((-self.a)*v))

    def calcular_deltinha(self, camada):
        deltinhas = []
        for valor in camada:

        print(deltinhas)


    def backpropagation(self):
        return

    def ajustar_pesos(self):
        return




