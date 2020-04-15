import time

from src.structures.Perceptron import Perceptron

"""
    Classe responsavel pelos processos da implementacao da Rede Neural*
    Functions:
     _init_(self,camada_entrada, tam_camada_escondida, tam_camada_saida, num_epocas, func_ativacao): Inicia os atributos da rede.
     treinar(self): Funcao que realiza o treinamento da rede, feedfoward e backpropagation.
     feedforward(self): Responsavel pelo feedforward.
     backpropagation(self): Responsavel pelo backpropagation acoplado ao ajuste de pesos.
     __calcular_informacao_erro(self, camada, erros_entrada=[]): Calcula a informacao de erro de acordo com a camada* e com os erros de cada entrada.
     __calcular_correcao_pesos(self, camada, perceptron_iterando, erros): Calcula a variacao do peso de acordo com o erro calculado e do peso atual da rede.
     __ajustar_pesos(self, camada, correcao_pesos): Realiza a alteracao dos pesos apos o backpropagation
     __inicializar_camada(camada): Inicia o processo de inicializacao da camada de acordo com a camada*.

    *camada: de entrada, de saída ou escondida.
    
    *Dado que trabalhamos com este formato de perceptron adotado nesta rede, podemos considerar todos os
    neuronios da camada de saída como classes de perceptrons dado os procedimentos de operação realizados
    pelo perceptron ser adaptativo para a atender a necessidade dos dois tipos de neurônios
    (escondido e de saída) em ambos os fluxos (feedforward e backpropagation).
    
    A defasagem principal da implementaçao em questao e a falta de uma classe especifica de logger
    dado que poluiu muito a parte do backpropagation e do proprio Main.
"""
class RedeNeural:
    def __init__(self, taxa_aprendizado, num_nos_camada_entrada, num_camadas_escondidas,
                 num_nos_camada_escondida, num_nos_camada_saida):

        self.target = '' # Variável apenas com criação para log
        self.problema = '' # Variável apenas com criação para log

        self.camada_entrada = []
        self.taxa_aprendizado = taxa_aprendizado
        self.num_nos_camada_entrada = num_nos_camada_entrada
        self.num_camadas_escondidas = num_camadas_escondidas
        self.num_nos_camada_escondida = num_nos_camada_escondida
        self.num_nos_camada_saida = num_nos_camada_saida
        self.camadas_escondidas = self.__inicializar_camada('escondida')
        self.camada_saida = self.__inicializar_camada('saida')

    """
        Algoritmo que centralizar todos os processos internos de treino da rede, do começo ao fim.
        1. Recebimento das entradas a serem consideradas para treinamento
        2. Etapa inicial de feedforward, calculando entradas ponderadas e valores de saída
    """
    def treinar(self, epocas, target, sample, target_description):
        for epoca in range(epocas):
            self.target = target
            self.camada_entrada = sample
            self.feedforward()
            self.backpropagation(target_description)

    """
        Feedforward que calcula a entrada ponderada de cada perceptron de sua camada escondida e de saida
        apenas invocando a funçao calcular_entrada_total que se encontra na classe perceptron para seus devidos
        valores de entrada e, em seguida, invoca o calcular_saida de cada perceptron aplicado a funcao de
        ativacao
    """
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

    """
        método responsável por realizar toda a retropropagaçao de acordo com a rede tendo todas suas
        entradas ponderadas calculadas para cada percetron junto ao seus valores de saída.
        O método calcula os erros e armazena todos de forma respectiva a representação gráfica em arrays,
        de forma que as informaçoes de erro de todos os perceptrons da camada de saida se encontram na posiçao
        [ultimo indice] do array erros, lembrando que este valor também é um array que contem todos os valores
        de saida. O mesmo vale para o calculo da correcao de pesos, cujo todos os pesos sao armazenados da mesma
        forma em array de arrays para recuperaçao posterior facilitada no ajuste do pesos
    """
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

    """
       Metodo responsavel por realizar o teste final simulando a aplicacao de fato dos valores de teste
       de acordo com o ajuste de pesos e processos feitos no treinamento da rede neural.
       Sendo apenas a etapa de feedforward e o respectivo log dos resultados. 
    """
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

    """
        Método responsável por calcular a informacao de erro de acordo com a camada recebida.
        O parâmetro da camada a ser calculada sendo recebido facilita a unicidade e futura chamada 
        do método para calcular todos os perceptrons de forma a encapsular a iteracao dos perceptrons ao 
        invés de externalizá-la 
    """
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
        return erros

    """
        Metodo responsavel por calcular a correcao de pesos com iteracao interna entre os perceptrons para calculo
        unico e armazenamento de forma que seja respectivo aos pesos e camadas a serem ajustados corretamente no futuro
        pelo acesso do ajuste de pesos
    """
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

    """
        Calculo e ajuste do pesos de acordo com matriz de correcao de pesos previamente calculada
    """
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

    """
        Inicializacao da camada e de seus respectivos perceptrons de acordo com o numero definido no arquivo Main.
        A inicializacao aleatoria dos pesos e do objeto Perceptron em si podem ser vistar na classe Perceptron.py
    """
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
