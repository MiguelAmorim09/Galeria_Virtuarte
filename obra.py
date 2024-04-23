from tkinter import *

class Obra:
    def __init__(self, gravar:bool, nomeArquivo):
        self.abertoGravar = gravar
        self.arquivo      = nomeArquivo
        
    def ler_campos_do_arquivo(self):
        if not self.abertoGravar:
            with open(self.arquivo, 'r') as arquivo:
                if not hasattr(self, 'posicao_arquivo'):
                    self.posicao_arquivo = 0
                    
                arquivo.seek(self.posicao_arquivo)
                
                umaLinha = arquivo.readline()
                
                self.posicao_arquivo = arquivo.tell()

                self.anoObra    = umaLinha[0:4]
                self.mesObra    = umaLinha[4:7]
                self.autorObra  = umaLinha[7:28]
                self.nomeObra   = umaLinha[28:59]
                self.estiloObra = umaLinha[59:75]
                self.valorObra  = umaLinha[75:86]
                self.urlObra    = umaLinha[86:]

                
            
    def gravar_campos_do_arquivo(self):
        if self.abertoGravar:
            linha = f'{self.anoObra}\t{self.mesObra}\t{self.autorObra}\t{self.nomeObra}\t{self.estiloObra}\t{self.valorObra}\t{self.urlObra}\n'
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
        self.arquivo.close()

    def __str__(self) -> str:
        return f'{self.anoObra}{self.mesObra}{self.autorObra}{self.nomeObra}{self.estiloObra}{self.valorObra}{self.urlObra}\n'
            
    def compararCom(self):
        pass