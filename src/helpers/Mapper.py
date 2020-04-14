import csv
from src.env import ARQUIVO_DE_LEITURA


class Mapper:
    def __init__(self):
        self._arquivo = self.handle_input()

    @staticmethod
    def handle_input():
        result = []
        caminho_arquivo = '../inputs/' + ARQUIVO_DE_LEITURA
        with open(caminho_arquivo, 'rt', encoding="utf-8-sig") as data:
            dados_arquivo = csv.reader(data)
            for linha in dados_arquivo:
                letra = linha[-1]
                dados_letra = linha[0:len(linha)-1]
                result.append({
                    'i': letra,
                    'valor': dados_letra
                })
        return result
        
    @property
    def arquivo(self):
        return self._arquivo

    @arquivo.setter
    def arquivo(self, value):
        self._arquivo = value

