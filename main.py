import os
import obra
from tkinter import * 
from tkinter import filedialog

def click(anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado):
    global ano, mes, autor, nome, estilo, valor, url
    ano    = anoDigitado.get()
    mes    = mesDigitado.get()
    autor  = autorDigitado.get()
    nome   = nomeDigitado.get()
    estilo = estiloDigitado.get()
    valor  = valorDigitado.get()
    url    = urlDigitado.get()
    
def dados():
    janela = Tk()
    
    textData =   Label  (janela, text='Data:')
    textAutor =  Label  (janela, text='Autor:')
    textNome =   Label  (janela, text='Nome:')
    textEstilo = Label  (janela, text='Estilo:')
    textValor =  Label  (janela, text='Valor:')
    textURL =    Label  (janela, text='URL:')
    
    textData.grid   (column=0, row=0)
    textAutor.grid  (column=0, row=1)
    textNome.grid   (column=0, row=2)
    textEstilo.grid (column=0, row=3)
    textValor.grid  (column=0, row=4)
    textURL.grid    (column=0, row=5)
    
    anoDigitado    = Entry  (janela, width=4)
    mesDigitado    = Entry  (janela, width=2)
    autorDigitado  = Entry  (janela, width=20)
    nomeDigitado   = Entry  (janela, width=20)
    estiloDigitado = Entry  (janela, width=15)
    valorDigitado  = Entry  (janela, width=10)
    urlDigitado    = Entry  (janela, width=20)
    
    anoDigitado.grid    (column=1, row=0, sticky='W')
    mesDigitado.grid    (column=1, row=0)
    autorDigitado.grid  (column=1, row=1)
    nomeDigitado.grid   (column=1, row=2)
    estiloDigitado.grid (column=1, row=3, sticky='W')
    valorDigitado.grid  (column=1, row=4, sticky='W')
    urlDigitado.grid    (column=1, row=5)
    
    botao = Button(janela, text='Enviar', command=lambda: [click(anoDigitado, mesDigitado, autorDigitado, nomeDigitado, estiloDigitado, valorDigitado, urlDigitado), janela.destroy()])
    botao.grid(column=1, row=6, sticky='W')
    
    janela.mainloop()

def seletor():
    print   ('\t--Galeria Virtuarte--\t')
    input   ('Pressione ENTER para continuar')
    print   ('\n\nCadastrar obra : 1')
    print   ('Listagem de obras : 2')
    print   ('Relatorio HTML : 3')
    print   ('Triangulo de Pascal : 4')
    print   ('\nTerminar : 0')
    
    escolha = input('\nDigite sua opcao:')
    return escolha

def realizar(opcaoDesejada:str):
    def op1():
        os.system('cls') or None
        print('\t--Cadastro de Obras--\t')
        input('Pressione ENTER para continuar')
        gravar = True
        arquivo = filedialog.askopenfilename(title='Escolher arquivo')
        cadastro = obra.Obra(gravar, arquivo)
        dados()
        cadastro.preencher_campos(ano, mes, autor, nome, estilo, valor, url)
        cadastro.gravar_campos_do_arquivo()
    
    def op2():
        os.system('cls') or None
        print('\t--Listagem de obras--\t')
        input('Pressione ENTER para continuar')
        gravar = False
        arquivo = filedialog.askopenfilename(title='Escolher arquivo')
        cadastro = obra.Obra(gravar, arquivo)
        cadastro.ler_campos_do_arquivo()
        print('Ano Mes Autor\t\t     Nome da Obra\t\t    Estilo\t       Valor   URL')
        cadastro.__str__()
        
    def op3():
        os.system('cls') or None    
        print('\t--Relatorio HTML--\t')
        input('Pressione ENTER para continuar')
        gravar = False
        arquivo = filedialog.askopenfilename(title='Escolher arquivo')
        relatorio = obra.Obra(gravar, arquivo)
        relatorio.ler_campos_do_arquivo()
    
    def op4():
        pass
    
    match opcaoDesejada:
        case    '1': op1()
        case    '2': op2()
        case    '3': op3()
        case    '4': op4()

def principal():
    escolha = 'x'
    while escolha != '0':
        escolha = seletor()
        if escolha != '0':
            realizar(escolha)
    print('Obrigado por utilizar o programa!')
    input('Pressione ENTER para terminar')

if __name__ == '__main__':
    os.system('cls') or None
    principal()