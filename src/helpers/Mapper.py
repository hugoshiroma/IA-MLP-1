"""
    Essa classe é responsável por mapear os arquivos para teste e arquivos para treino,
    tratando as respostas esperadas para o problema e gerando dicionarios para melhor manipulá-los

"""

import csv
from src.env import ARQUIVOS_PARA_TREINO, ARQUIVOS_PARA_TESTE


class Mapper:
    def __init__(self):
        self._arquivos = self.get_multiple_files()
        self.arquivos_teste = self.get_test_file()

    @property
    def arquivos(self):
        return self._arquivos

    @arquivos.setter
    def arquivos(self, value):
        self._arquivos = value

    def get_multiple_files(self):
        result = []
        for arquivo in ARQUIVOS_PARA_TREINO:
            result.append(self.handle_input(arquivo))
        return result

    def get_test_file(self):
        result = []
        for arquivo in ARQUIVOS_PARA_TESTE:
            result.append(self.handle_input(arquivo))
        return result

    """
        O método abaixo transforma os arquivos csvs em dicionários de dados
    """
    def handle_input(self, filename):
        inputs = []
        caminho_arquivo = '../inputs/Part-1/' + filename
        with open(caminho_arquivo, 'rt', encoding="utf-8-sig") as data:
            dados_arquivo = csv.reader(data)

            for linha in dados_arquivo:
                target = self.get_target(linha[-1])
                sample = linha[:-1]
                inputs.append({
                    'target_description': linha[-1],
                    'target': target,
                    'sample': sample
                })

            result = {'nome_problema': filename[:-4],
                      'inputs': inputs}
        return result

    """
        O método abaixo retorna a resposta esperada de acordo com um target
    """

    def get_target(self, target):
        dict = {
            'A': [1, -1, -1, -1, -1, -1, -1],
            'B': [-1, 1, -1, -1, -1, -1, -1],
            'C': [-1, -1, 1, -1, -1, -1, -1],
            'D': [-1, -1, -1, 1, -1, -1, -1],
            'E': [-1, -1, -1, -1, 1, -1, -1],
            'J': [-1, -1, -1, -1, -1, 1, -1],
            'K': [-1, -1, -1, -1, -1, -1, 1],
            '0': [0],
            '1': [1]
        }

        """
             O target dos outros problemas é transformado em lista para que a rede seja
            genérica para todos os problemas em questão
        """

        return dict[target]
