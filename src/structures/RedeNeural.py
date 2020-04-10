from src.env import NUMERO_DE_NOS_CAMADA_ESCONDIDA, NUMERO_DE_CAMADAS_ESCONDIDAS, NUMERO_DE_NOS_CAMADA_SAIDA, \
    NUMERO_DE_EPOCAS, RESPOSTAS_ARQUIVO_DE_LEITURA, TAXA_DE_APRENDIZADO
from src.structures.Perceptron import Perceptron


class RedeNeural:
    def __init__(self):
        self.target = ''
        self.camada_entrada = []
        self.camadas_escondidas = self.__inicializar_camada('escondida')
        self.camada_saida = self.__inicializar_camada('saida')

    def treinar(self, letra, valor_entrada):
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

            if camada is NUMERO_DE_CAMADAS_ESCONDIDAS-1:
                for perceptron in range(NUMERO_DE_NOS_CAMADA_SAIDA):
                    self.camada_saida[perceptron].calcular_entrada_total(self.camadas_escondidas[camada])
                    self.camada_saida[perceptron].calcular_saida()

        self.__backpropagation()

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

    def __backpropagation(self):
        erros = []
        pesos_a_corrigir = []
        biass_a_corrigir = []
        somas = []
        valor_erros = []
        variacao_de_peso_entradas = []
        variacao_de_biass = []
        for perceptron in range(len(self.camada_saida)):
            info_erro = (RESPOSTAS_ARQUIVO_DE_LEITURA.get(self.target)[perceptron] - self.camada_saida[perceptron].saida) * self.camada_saida[perceptron].aplicar_funcao_ativacao_derivada(self.camada_saida[perceptron].entrada_total)
            erros.append(info_erro)

        i = NUMERO_DE_CAMADAS_ESCONDIDAS - 1
        for perceptron in range(len(self.camadas_escondidas[i])):
            correcao_de_pesos = []
            for perceptron_saida in range(len(self.camada_saida)):
                correcao_de_peso = TAXA_DE_APRENDIZADO * self.camada_saida[perceptron_saida].saida * erros[perceptron]
                correcao_de_pesos.append(correcao_de_peso)
            pesos_a_corrigir.append(correcao_de_pesos)

        for perceptron in range(len(self.camada_saida)):
            bias_a_corrigir = TAXA_DE_APRENDIZADO * self.camada_saida[perceptron].saida
            biass_a_corrigir.append(bias_a_corrigir)

        i = NUMERO_DE_CAMADAS_ESCONDIDAS - 1
        soma = 0

        for perceptron in range(len(self.camadas_escondidas[i])):
            for peso in self.camadas_escondidas[i][perceptron].pesos_entrada:
                soma += erros[perceptron] * peso
            somas.append(soma)

        for perceptron in range(len(self.camadas_escondidas[i])):
            erro = somas[perceptron] * self.camadas_escondidas[i][perceptron].aplicar_funcao_ativacao_derivada(self.camadas_escondidas[i][perceptron].entrada_total)
            valor_erros.append(erro)

        for erro in valor_erros:
            variacao_peso_entrada = []
            for entrada in self.camada_entrada:
                variacao_peso_entrada.append(TAXA_DE_APRENDIZADO * erro * float(entrada))
            variacao_de_peso_entradas.append(variacao_peso_entrada)

        i = NUMERO_DE_CAMADAS_ESCONDIDAS - 1
        for erro in valor_erros:
            variacao_de_bias = TAXA_DE_APRENDIZADO * erro
            variacao_de_biass.append(variacao_de_bias)

        for perceptron in self.camada_saida:
            for peso in perceptron.pesos_entrada:
                test = pesos_a_corrigir[perceptron.pesos_entrada.index(peso)][self.camada_saida.index(perceptron)]
                peso += pesos_a_corrigir[perceptron.pesos_entrada.index(peso)][self.camada_saida.index(perceptron)]

        for camada in self.camadas_escondidas:
            for perceptron in camada:
                for peso in perceptron.pesos_entrada:
                    peso += variacao_de_peso_entradas[camada.index(perceptron)][perceptron.pesos_entrada.index(peso)]

        print('')
        # def __calcular_gradiente_local():
        #
