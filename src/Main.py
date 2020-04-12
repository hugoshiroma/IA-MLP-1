from src.env import NUMERO_DE_EPOCAS
from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural


inputs = Mapper().arquivo
rede_neural = RedeNeural()
for epoca in range(NUMERO_DE_EPOCAS):
    for input in inputs:
        rede_neural.treinar(input['i'], input['valor'])

for perceptron in rede_neural.camada_saida:
    print('saida', rede_neural.camada_saida.index(perceptron))
    print(perceptron.saida*1000)
