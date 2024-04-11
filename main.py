import os
import obra
from tkinter import filedialog as fd
from tkinter import *

def seletor() -> str:
    print('--Galeria Virtuarte--')
    input('Pressione ENTER para continuar')
    

    print('aaaaaa')
    print('\n\nCadastrar obra : 1')
    print('Listagem de obras : 2')
    
    print('\nTerminar : 0')
    
    escolha = input('\nDigite a opcao desejada:')
    os.system('cls') or None
    return escolha

def realizar(opcaoDesejada:str):  
    def op1():
        def click():
            global anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado
            anoDigitado = ano.get().ljust(4)
            mesDigitado = mes.get().ljust(2)
            autorDigitado = autor.get().ljust(20)
            nomeDigitado = nome.get().ljust(20)
            estiloDigitado = estilo.get().ljust(15)
            valorDigitado = valor.get()
            urlDigitado = url.get().ljust(100)
            janela.destroy()
            cadastro.gravarCamposNoArquivo(anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado)

        global janela, ano, mes, autor, nome, estilo, valor, url
        print('-Cadastro de Obras--')
        input('Pressione ENTER para continuar')
        gravar = True
        arquivo = fd.askopenfilename()
        cadastro = obra.Obra(gravar, arquivo)

        janela = Tk()
        janela.title('Dados da obra')

        textData = Label(janela, text='Data:')
        textData.grid(column=0, row=0)

        ano = Entry(janela, width='4')
        ano.grid(column=1, row=0, sticky='W')

        mes = Entry(janela, width='2')
        mes.grid(column=1, row=0)

        textAutor = Label(janela, text='Autor:')
        textAutor.grid(column=0, row=1)

        autor = Entry(janela, width='20')
        autor.grid(column=1, row=1)

        textNome = Label(janela, text='Nome:')
        textNome.grid(column=0, row=2)

        nome = Entry(janela, width='20')
        nome.grid(column=1, row=2, columnspan=2)

        textEstilo = Label(janela, text='Estilo:')
        textEstilo.grid(column=0, row=3)

        estilo = Entry(janela, width='15')
        estilo.grid(column=1, row=3, sticky='W')

        textValor = Label(janela, text='Valor:')
        textValor.grid(column=0, row=4)

        valor = Entry(janela, width='10')
        valor.grid(column=1, row=4, sticky='W')

        textURL = Label(janela, text='URL:')
        textURL.grid(column=0, row=5)

        url = Entry(janela, width='20')
        url.grid(column=1, row=5)

        botao = Button(text='Enviar', command=click)
        botao.grid(column=1, row=6)
        janela.mainloop()
        
        input('Pressione ENTER para voltar ao seletor')
        cadastro.fecharArquivo()

    def op2():
        print('--Listagem de obras--')
        input('Pressione ENTER para continuar')
        gravar = False
        arquivo = fd.askopenfilename()
        cadastro = obra.Obra(gravar, arquivo)
        cadastro.lerCamposDoArquivo()
        cadastro.__str__()
        linhas = int()
        for i in range(linhas):
            print(cadastro.__str__())

    match opcaoDesejada:
        case    '1': op1()
        case    '2': op2()
        
def principal():
    escolha = 'x'
    while escolha != '0':   
        escolha = seletor()
        if escolha != '0':
            realizar(escolha)
    print('Obrigado por utilizar esse programa!')
    input('Pressione ENTER para continuar')
    os.system('cls') or None

if __name__ == '__main__':
    os.system('cls') or None
    principal()
