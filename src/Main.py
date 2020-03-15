from src import rede_neural as rn, datasets


caracteres_limpos = datasets.get_caracteres_limpo()
# cada linha do dataset tem um CONJUNTO de neurônios de entrada, que é o que vai ser mandado pra rede neural para
# poder classificar essa linha
for caracter in caracteres_limpos:
    rn.classificar(caracter)




