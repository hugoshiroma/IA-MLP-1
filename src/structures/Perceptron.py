import random
import numpy as np

"""
    Classe responsavel por manter as funcoes que definem e ajustam um perceptron*
    Functions:
        _init_(self,camada): Inicia os valores do perceptron de acordo com a camada*.
        calcular_entrada_total(self,entradas): Recebe os valores que serao utilizados para o input ou para a camada de saida e retorna a entrada total.
        calcular_saida(self): Aplica a funcao de ativacao no valor da entrada total retorna a saída.
        aplicar_funcao_ativacao(valor): Define a funcao de ativacao e aplica utilizando o parametro.
        aplicar_funcao_ativacao_derivada(self, valor): Aplica a funcao de ativacao derivada utilizando o parametro.
        __inicializar_pesos(camada): Inicializa os pesos de acordo com a camada*.
        __ajustar_pesos(self): Ajusta os pesos ao final do treinamento da rede.
        *camada: de entrada, de saída ou escondida.
        
    *A classe perceptron considera para sua implementação base o armazenamento dos pesos entrantes, ou seja,
    cada perceptron recebe vários valores de entrada pois são os pesos a serem recebidos, facilitando assim
    os passos 3 e 4 do algoritmo visto em aula, dado a iteração prática pelos pesos e valores para o somatório.
"""
class Perceptron:
    def __init__(self, num_nos_conectados):
        self.entrada = 0
        self.entrada_total = 0
        self.num_nos_conectados = num_nos_conectados
        self.pesos_entrada = self.__inicializar_pesos()
        self.saida = 0

    """
     O método calcular_entrada_total itera sobre cada valor de entrada e seu respectivo peso recebidos
     neste Percetron e calcula o valor de soma de suas entradas ponderadas
    """
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

    """
     O método aplicar_funcao_ativacao_derivada retorna o cálculo do valor da derivada de deslocamento
     das entradas ponderadas referente ao seu gradiente local de erro
    """
    def aplicar_funcao_ativacao_derivada(self, valor):
        return self.aplicar_funcao_ativacao(valor) * (1 - self.aplicar_funcao_ativacao(valor))

    def __inicializar_pesos(self):
        pesos = []
        for i in range(self.num_nos_conectados):
            pesos.append(random.randrange(-1, 2))
        return pesos
