

# por enquanto estou considerando que sempre será mandado uma lista onde o último item é a resposta esperada
def classificar(dado):
    # basicamente é aqui que vai ficar o algoritmo do MPL
    target = dado[-1]
    neuronios = dado[0:63]
    print(target, neuronios)
    # aqui imagino que o classificar devera retornar o valor dos pesos, o treinamento é feito nessa função
