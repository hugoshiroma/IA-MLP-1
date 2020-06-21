"""
    Classe responsavel por fazer o mapeamento dos arquivos .csv para teste e para treino da rede
    tratando as respostas esperadas para o problema e gerando dicionarios para melhor manipula-los

    Functions:
        init(self): Inicializa a classe Mapper que le todos os arquivos dispostos na pasta 'inputs', considerando que
            todos os arquivos são .csv, que possuem uma amostra por linha e que o target se encontra na ultima posicao
            da linha;
        get_train_files():
        handle_input: Le o arquivo .csv retornando um dicioncario de dados para ser usado na rede neural.
        arquivo(self): Funcao que guarda o objeto do retorno da funcao 'handle_input' na variavel _arquivo.
        arquivo(self,value): Funcao que 'seta' os valores do objeto guardado pela funcao 'arquivo(self)' na variavel _arquivo.
        get_target(self, target): Funcao que retorna o valor esperado dentro da rede de acordo com o target alfanumerico

"""

import csv
from src.env import ARQUIVOS_PARA_TREINO, ARQUIVOS_PARA_TESTE, TARGETS


class Mapper:
    def __init__(self):
        self._arquivos_treino = self.get_train_files()
        self._arquivos_teste = self.get_test_files()

    def get_train_files(self):
        result = []
        for arquivo in ARQUIVOS_PARA_TREINO:
            result.append(self.handle_input(arquivo))
        return result

    def get_test_files(self):
        result = []
        for arquivo in ARQUIVOS_PARA_TESTE:
            result.append(self.handle_input(arquivo))
        return result

    def handle_input(self, filename):
        inputs = []
        caminho_arquivo = '../inputs/' + filename
        with open(caminho_arquivo, 'rt', encoding="utf-8-sig") as data:
            dados_arquivo = csv.reader(data)
            for linha in dados_arquivo:
                inputs.append({
                    'target': linha[-1],
                    'sample': linha[:-1],
                    'target_value': self.get_target_value(filename, linha[-1])
                })

            result = {'filename': filename[:-4],
                      'inputs': inputs}
        return result

    def get_target_value(self, filename, target):
        return TARGETS[filename][target]

    @property
    def arquivos_treino(self):
        return self._arquivos_treino

    @arquivos_treino.setter
    def arquivos_treino(self, value):
        self._arquivos_treino = value

    @property
    def arquivos_teste(self):
        return self._arquivos_teste

    @arquivos_teste.setter
    def arquivos_teste(self, value):
        self._arquivos_teste = value