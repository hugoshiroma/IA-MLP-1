from src import rede_neural as rn, camada_entrada


caracteres_limpos = camada_entrada.get_caracteres_limpo()
# cada linha do dataset tem um CONJUNTO de neurônios de entrada, que é o que vai ser mandado pra rede neural para
# poder treinar essa linha
for caracter in caracteres_limpos:
    rn.treinar(caracter)




