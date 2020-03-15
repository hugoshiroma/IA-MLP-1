import os
import csv
import pathlib
import src.env

inputsDir = pathlib.Path(__file__).parent.parent.absolute().joinpath(pathlib.PurePosixPath('inputs'))
inputLength = src.env.INPUT_LENGTH


class Mapper:
    def __init__(self, input_folder='Part-1'):
        self._files = self.handle_input(self, input_folder)

    @staticmethod
    def handle_input(self, input_folder):
        result = []
        for dirs, subdir, files in os.walk(inputsDir):
            for file in files:
                file_path = '../inputs/' + input_folder + '/' + file
                with open(file_path, 'rt', encoding="utf-8-sig") as data:
                    file_data = csv.reader(data)
                    for line in file_data:
                        if line[-1].isalpha():
                            char_line = 1
                            letter = line[-1]
                            char_matrix = []
                            while char_line <= 7:
                                char_matrix.append(line[(char_line - 1) * inputLength:char_line * inputLength])
                                char_line += 1
                            result.append({
                                'index': letter,
                                'value': char_matrix
                            })
        return result
        
    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value

