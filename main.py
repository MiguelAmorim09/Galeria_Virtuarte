import os
import obra
from tkinter import * 
from tkinter import filedialog

def html():
   with open('obras.html', 'w') as pagina:
    
    pagina.write('<!DOCTYPE html>\n')
    pagina.write('<html lang="en">\n')
    pagina.write('<head>\n')
    pagina.write('\t<meta charset="UTF-8">\n')
    pagina.write('\t<meta name="viewport" content="width=device-width, inital-scale=1.0">\n')
    pagina.write('\t<title>Document</title>\n')
    pagina.write('</head>\n')
    pagina.write('<body>\n')
    
    pagina.write    ('\t<table>\n')
    
    pagina.write        ('\t\t<tr>\n')
    pagina.write            ('\t\t\t<th colspan="6">RELATORIO DE OBRAS GALERIA VIRTUAL</th>\n')
    pagina.write        ('\t\t</tr>\n')
    
    pagina.write        ('\t\t<tr>\n')
    pagina.write            ('\t\t\t<th>Ano/Mes</th>\n')
    pagina.write            ('\t\t\t<th>Nome</th>\n')
    pagina.write            ('\t\t\t<th>Estilo</th>\n')
    pagina.write            ('\t\t\t<th>Autor</th>\n')
    pagina.write            ('\t\t\t<th>Valor</th>\n')
    pagina.write            ('\t\t\t<th>Imagem</th>\n')
    pagina.write        ('\t\t</tr>\n')
    
    pagina.write    ('\t</table>\n')
    
    pagina.write('</body>\n')
    pagina.write('</html>\n')

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
    os.system('cls') or None
    print   ('\t--Galeria Virtuarte--\t')
    input   ('Pressione ENTER para continuar')
    print   ('\n\nCadastro de obras de arte : 1')
    print   ('Listagem de obras de arte : 2')
    print   ('Página web de obras de arte : 3')
    print   ('Triangulo de Pascal : 4')
    print   ('\nTerminar : 0')
    
    escolha = input('\nDigite sua opcao:')
    return escolha

def realizar(opcaoDesejada:str):
    def op1():
        os.system('cls') or None
        print   ('\t--Cadastro de Obras--\t')
        input   ('Pressione ENTER para continuar')
        os.system('cls') or None
        gravar = True
        arquivo = filedialog.askopenfilename(title='Escolher arquivo')
        cadastro = obra.Obra(gravar, arquivo)
        dados()
        cadastro.preencher_campos(ano, mes, autor, nome, estilo, valor, url)
        cadastro.gravar_campos_do_arquivo()
        input('Pressione ENTER para continuar')
    
    def op2():
        os.system('cls') or None
        print   ('\t--Listagem de obras--\t')
        input   ('Pressione ENTER para continuar')
        os.system('cls') or None
        gravar = False
        arquivo = filedialog.askopenfilename(title='Escolher arquivo')
        cadastro = obra.Obra(gravar, arquivo)
        cadastro.ler_campos_do_arquivo()
        print('Ano  Mes Autor\t\t      Nome da Obra\t\t     Estilo\t\tValor    URL')
        cadastro.__str__()
        input('Pressione ENTER para continuar')
        
    def op3():
        os.system('cls') or None    
        print   ('\t--Relatorio HTML--\t')
        input   ('Pressione ENTER para continuar')
        os.system('cls') or None
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
    print   ('Obrigado por utilizar o programa!')
    input   ('Pressione ENTER para terminar')

if __name__ == '__main__':
    os.system('cls') or None
    principal()