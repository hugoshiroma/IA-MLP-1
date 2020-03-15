import csv
# a ideia é ter um arquivo que reúna todos os datasets
# comecei a fazer com lista, mas podemos trocar se encontrarmos uma estrutra melhor (um dicionario, um dataframe...)


def get_caracteres_limpo():
    with open('..\inputs\Part-1\caracteres-limpo.csv', 'rt', encoding="utf-8-sig")as csvCaracteresLimpo:
        csv_caracteres_limpo = csv.reader(csvCaracteresLimpo)
        return list(csv_caracteres_limpo)  # cada linha do dataset vira um objeto da lista


def get_caracteres_ruido():
    with open('..\inputs\Part-1\caracteres-ruido.csv', 'rt', encoding="utf-8-sig")as csvCaracteresRuido:
        csv_caracteres_ruido = csv.reader(csvCaracteresRuido)
        return list(csv_caracteres_ruido)  # cada linha do dataset vira um objeto da lista



# with open('..\inputs\Part-1\problemAND.csv','rt', encoding="utf-8-sig")as csvAND:
#   arquivoAND = csv.reader(csvAND)
#   print("Arquivo AND")
#   for linha in arquivoAND:
#         print(linha)
#
#
# with open('..\inputs\Part-1\problemOR.csv','rt', encoding="utf-8-sig")as csvOR:
#   arquivoOR = csv.reader(csvOR)
#   print("Arquivo OR")
#   for linha in arquivoOR:
#         print(linha)
#
#
# with open('..\inputs\Part-1\problemXOR.csv','rt', encoding="utf-8-sig")as csvXOR:
#   arquivoXOR = csv.reader(csvXOR)
#   print("Arquivo XOR")
#   for linha in arquivoXOR:
#         print(linha)