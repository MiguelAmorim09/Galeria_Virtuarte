from tkinter import *

class Obra:
    def __init__(self, gravar:bool, nomeArquivo):
        self.abertoGravar = gravar
        self.arquivo      = nomeArquivo
        
    def ler_campos_do_arquivo(self):
        if not self.abertoGravar:
            with open(self.arquivo, 'r') as arquivo:
                self.linhas = arquivo.read()
            
    def gravar_campos_do_arquivo(self):
        if self.abertoGravar:
            linha = f'{self.anoObra} {self.mesObra} {self.autorObra} {self.nomeObra} {self.estiloObra} {self.valorObra} {self.urlObra}\n'
            with open(self.arquivo, 'a', encoding='utf-8') as arquivo:
                arquivo.write(linha)

    def preencher_campos(self, ano, mes, autor, nome, estilo, valor, url):
        self.anoObra    = ano.ljust(4)
        self.mesObra    = mes.rjust(2, '0')
        self.autorObra  = autor.ljust(20)
        self.nomeObra   = nome.ljust(20)
        self.estiloObra = estilo.ljust(15)
        self.valorObra  = valor
        self.urlObra    = url.ljust(100)

    def fechar_arquivo(self):       #nao achei necessario o fechamento do arquivo,
        pass                        #ja que com with ele se fecha sozinho

    def __str__(self):
        return f'{self.anoObra} {self.mesObra} {self.nomeObra} {self.autorObra} {self.valorObra} {self.urlObra}'

    def compararCom(self):
        pass