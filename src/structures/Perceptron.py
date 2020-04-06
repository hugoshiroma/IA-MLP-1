from src.structures.No import No


class NoEscondido(No):
    def __init__(self, input_pesos):
        self.peso = self.calcular_peso(input_pesos)

    def calcular_peso(self, input_pesos):
        for peso in input_pesos:

