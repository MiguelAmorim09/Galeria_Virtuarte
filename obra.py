from tkinter import *

class Obra:
    def __init__(self, gravar:bool, nomeArquivo):
        self.abertoParaGravar = gravar
        self.arquivo = nomeArquivo
        
    def lerCamposDoArquivo(self):
        if not self.abertoParaGravar:
            with open(self.arquivo, 'r') as arquivo:
                self.ano = arquivo.read(4)
                self.mes = arquivo.read(2)
                self.autor = arquivo.read(20)
            
    def gravarCamposNoArquivo(self, anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
        if self.abertoParaGravar:
            with open(self.arquivo, 'w') as arquivo:
                arquivo.write(anoDigitado)
                arquivo.write(mesDigitado)
                arquivo.write(autorDigitado)
                arquivo.write(nomeDigitado)
                arquivo.write(estiloDigitado)
                arquivo.write(valorDigitado)
                arquivo.write(urlDigitado)

    def preencherCampos(self, anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write(f'\n{anoDigitado}')
            arquivo.write(mesDigitado)
            arquivo.write(autorDigitado)
            arquivo.write(nomeDigitado)
            arquivo.write(estiloDigitado)
            arquivo.write(valorDigitado)
            arquivo.write(urlDigitado)

    def fecharArquivo(self):
        pass

    def __str__(self):
        pass

    def compararCom():
        pass