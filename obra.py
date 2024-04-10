from tkinter import *

class Obra:
    def __init__(self, gravar:bool, nomeArquivo):
        self.abertoParaGravar = gravar
        self.arquivo = nomeArquivo
        
    def lerCamposDoArquivo(self):
        if not self.abertoParaGravar:
            with open(self.arquivo, 'r') as arquivo:
                self.ano = arquivo.read(5)
                self.mes = arquivo.read(2)
                self.autor = arquivo.read(20)
                self.nome = arquivo.read(20)
                self.estilo = arquivo.read(15)
                self.valor = arquivo.read(4)
                self.url = arquivo.read(100)
            
    def gravarCamposNoArquivo(self, anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
        if self.abertoParaGravar:
            with open(self.arquivo, 'a') as arquivo:
                arquivo.write(anoDigitado)
                arquivo.write(mesDigitado)
                arquivo.write(autorDigitado)
                arquivo.write(nomeDigitado)
                arquivo.write(estiloDigitado)
                arquivo.write(valorDigitado)
                arquivo.write(urlDigitado)

    def preencherCampos(self, anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write()
            arquivo.write()
            arquivo.write()
            arquivo.write()
            arquivo.write()
            arquivo.write()
            arquivo.write()

    def fecharArquivo(self):
        self.arquivo.close()

    def __str__(self):
        return f'{self.ano} {self.mes} {self.nome} {self.autor} {self.valor} {self.url}'

    def compararCom():
        pass