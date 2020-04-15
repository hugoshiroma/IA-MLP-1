import csv
from src.env import ARQUIVOS_PARA_TREINO


class Mapper:
    def __init__(self):
        self._arquivos = self.get_multiple_files()

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

    # TODO: (Bel) deixei o método não estático pra poder utilizar outros métodos dessa classe
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
        # O target dos outros problemas é transformado em lista para que a rede seja
        # genérica para todos os problemas em questão
        return dict[target]