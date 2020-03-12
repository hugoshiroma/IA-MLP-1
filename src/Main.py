import csv

with open('..\inputs\Part-1\problemAND.csv','rt', encoding="utf-8-sig")as csvAND:
  arquivoAND = csv.reader(csvAND)
  print("Arquivo AND")
  for linha in arquivoAND:
        print(linha)


with open('..\inputs\Part-1\problemOR.csv','rt', encoding="utf-8-sig")as csvOR:
  arquivoOR = csv.reader(csvOR)
  print("Arquivo OR")
  for linha in arquivoOR:
        print(linha)


with open('..\inputs\Part-1\problemXOR.csv','rt', encoding="utf-8-sig")as csvXOR:
  arquivoXOR = csv.reader(csvXOR)
  print("Arquivo XOR")
  for linha in arquivoXOR:
        print(linha)


with open('..\inputs\Part-1\caracteres-limpo.csv','rt', encoding="utf-8-sig")as csvCaracteresLimpo:
  arquivoCaracteresLimpo = csv.reader(csvCaracteresLimpo)
  print("Arquivo Caracteres Limpos")
  for linha in arquivoCaracteresLimpo:
        print(linha)

with open('..\inputs\Part-1\caracteres-ruido.csv','rt', encoding="utf-8-sig")as csvCaracteresRuido:
  arquivoCaracteresRuido = csv.reader(csvCaracteresRuido)
  print("Arquivo Caracteres Ruidosos")
  for linha in arquivoCaracteresRuido:
        print(linha)