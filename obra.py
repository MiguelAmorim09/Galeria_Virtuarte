from tkinter import *

class Obra:
    def __init__(self, gravar:bool, nomeArquivo):
        self.anoObra    = ''
        self.mesObra    = ''
        self.autorObra  = ''
        self.nomeObra   = ''
        self.estiloObra = ''
        self.valorObra  = ''
        self.urlObra    = ''
        self.abertoGravar = gravar
        self.arquivo      = nomeArquivo
        
    def ler_campos_do_arquivo(self):
        if not self.abertoGravar:
            with open(self.arquivo, 'r') as arquivo:
                self.anoObra    = arquivo.read(4)
                self.mesObra    = arquivo.read(3)
                self.autorObra  = arquivo.read(21)
                self.nomeObra   = arquivo.read(31)
                self.estiloObra = arquivo.read(16)
                self.valorObra  = arquivo.read(11)
                self.urlObra    = arquivo.read(101)
            
    def gravar_campos_do_arquivo(self):
        if self.abertoGravar:
            linha = f'{self.anoObra} {self.mesObra} {self.autorObra} {self.nomeObra} {self.estiloObra} {self.valorObra} {self.urlObra}\n'
            with open(self.arquivo, 'a', encoding='utf-8') as arquivo:
                arquivo.write(linha)

    def preencher_campos(self, ano, mes, autor, nome, estilo, valor, url):
        self.anoObra    = ano.ljust(4)
        self.mesObra    = mes.rjust(2, '0')
        self.autorObra  = autor.ljust(20)
        self.nomeObra   = nome.ljust(30)
        self.estiloObra = estilo.ljust(15)
        self.valorObra  = valor.rjust(10)
        self.urlObra    = url.ljust(100)

    def fechar_arquivo(self):
        pass

    def __str__(self) -> str:
        pass
    
    def compararCom(self):
        pass