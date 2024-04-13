import os
from tkinter import *
from tkinter import filedialog

def click(anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
    ano = anoDigitado.get().ljust(4)
    mes = mesDigitado.get().ljust(2)
    autor = autorDigitado.get().ljust(20)
    nome = nomeDigitado.get().ljust(20)
    estilo = estiloDigitado.get().ljust(15)
    valor = valorDigitado.get()
    url = urlDigitado.get().ljust(100)
    return ano, mes, autor, nome, estilo, valor, url

def dados():
    janela = Tk()
    
    textData =   Label(janela, text='Data:')
    textAutor =  Label(janela, text='Autor:')
    textNome =   Label(janela, text='Nome:')
    textEstilo = Label(janela, text='Estilo:')
    textValor =  Label(janela, text='Valor:')
    textURL =    Label(janela, text='URL:')
    
    textData.grid   (column=0, row=0)
    textAutor.grid  (column=0, row=1)
    textNome.grid   (column=0, row=2)
    textEstilo.grid (column=0, row=3)
    textValor.grid  (column=0, row=4)
    textURL.grid    (column=0, row=5)
    
    anoDigitado =    Entry(janela, width=4)
    mesDigitado =    Entry(janela, width=2)
    autorDigitado =  Entry(janela, width=20)
    nomeDigitado =   Entry(janela, width=20)
    estiloDigitado = Entry(janela, width=15)
    valorDigitado =  Entry(janela, width=10)
    urlDigitado =    Entry(janela, width=20)
    
    anoDigitado.grid    (column=1, row=0, sticky='W')
    mesDigitado.grid    (column=1, row=0)
    autorDigitado.grid  (column=1, row=1)
    nomeDigitado.grid   (column=1, row=2)
    estiloDigitado.grid (column=1, row=3, sticky='W')
    valorDigitado.grid  (column=1, row=4, sticky='W')
    urlDigitado.grid    (column=1, row=5)
    
    botao = Button(janela, text='Enviar', command=click(anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado))
    botao.grid(column=1, row=6, sticky='W')
    
    janela.mainloop()

def escolher_arquivo(janelaArquivo):
    arquivo = filedialog.askopenfilename(title='Escolher Arquivo')
    janelaArquivo.destroy()

def janela_arquivo():
    janelaArquivo = Tk()
    botaoArquivo = Button(text='Escolher', command=escolher_arquivo(janelaArquivo))
    botaoArquivo.grid(column=0, row=0)
    janelaArquivo.mainloop()

def seletor():
    print('--Galeria Virtuarte--')
    input('Pressione ENTER para continuar')
    print('\n\nCadastrar obra : 1')
    print('Listagem de obras : 2')
    print('\nTerminar : 0')
    
    escolha = input('\nDigite sua opcao:')
    return escolha

def realizar(opcaoDesejada:str):
    def op1():
        os.system('cls') or None
        print('--Cadastro de Obras--')
        input('Pressione ENTER para continuar')
        gravar = True
        dados()
    
    def op2():
        pass
    
    match opcaoDesejada:
        case    '1': op1()
        case    '2': op2()

def principal():
    os.system('cls') or None
    escolha = 'x'
    while escolha != '0':
        escolha = seletor()
        if escolha != '0':
            realizar(escolha)
    print('Obrigado por utilizar o programa!')
    input('Pressione ENTER para terminar')

principal()