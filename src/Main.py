from src.helpers.Mapper import Mapper
from src.structures.RedeNeural import RedeNeural


inputs = Mapper().arquivo
rede_neural = RedeNeural()
for input in inputs:
    rede_neural.treinar(input['i'], input['valor'])
    # tam_camada_escondida = 2
    # tam_camada_saida = 7
    # num_epocas = 100
    # func_ativacao = None
    # caracteres_limpos = camada_entrada.get_caracteres_limpo()
    #
    # rn = Rede.Rede(caracteres_limpos, tam_camada_escondida, tam_camada_saida, num_epocas, func_ativacao)
    # rn.treinar()

    # test = Mapper()
    # print(test.files[1]['value'])
