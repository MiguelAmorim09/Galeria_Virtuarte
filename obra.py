from tkinter import *

class Obra:
    def __init__(self, ano, mes, autor, nome, estilo, valor:float, url,  gravar:bool, NomeArquivo):
        self.ano = ano
        self.mes = mes
        self.autor = autor
        self.nome = nome
        self.estilo = estilo
        self.valor = valor
        self.url = url
        self.abertoParaGravar = gravar
        self.arquivo = open(NomeArquivo, 'r')
        
    def lerCamposDoArquivo(self):
        if not self.abertoParaGravar:
            with open('obras.txt', 'r') as arquivo:
                pass
            
    def gravarCamposNoArquivo(self):
        if self.abertoParaGravar:
            with open('obras.txt', 'a') as arquivo:
                arquivo.write(self.ano)
                arquivo.write(self.mes)
                arquivo.write(self.autor)
                arquivo.write(self.nome)
                arquivo.write(self.estilo)
                arquivo.write(self.valor)
                arquivo.write(self.url)