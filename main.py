import os
import obra, mat
from tkinter import filedialog    
import webbrowser
    
def op1():
    print('\t--Cadastro de Obras--\t')
    tecla = input('Presione ENTER para continuar')
    os.system('cls') or None
    
    gravar = True
    arquivo = filedialog.askopenfilename(title='Escolher arquivo')
    cadastro = obra.Obra(gravar, arquivo)
    
    print('Digite os dados da obra referente ao que é pedido\nSe desejar sair do cadastro, digite 0 no valor do ano\n')
    tecla   = input('\n\tPressione ENTER para continuar\t')
    ano = ''
    while ano != '0':
        ano     = input('Ano da obra:')
        mes     = input('Mês da obra:')
        autor   = input('Autor da obra:')
        nome    = input('Nome da obra:')
        estilo  = input('Estilo da obra:')
        valor   = input('Valor da obra:')
        url     = input('URL da obra:')
        
        if ano != '0':
            cadastro.preencher_campos(ano, mes, autor, nome, estilo, valor, url)
            cadastro.gravar_campos_do_arquivo()
        else:
            pass
    
    input('Pressione ENTER para continuar')
    cadastro.fechar_arquivo()
    os.system('cls') or None
    
def op2():
    print   ('\t--Listagem de obras--\t')
    tecla = input('Presione ENTER para continuar')
    os.system('cls') or None
    
    gravar = False
    arquivo = filedialog.askopenfilename(title='Escolher arquivo')
    listar = obra.Obra(gravar, arquivo)
    
    print('Ano\tMês\tAutor\t\t\tNome da Obra\t\t\tEstilo\t\t   Valor\tURL')
    obras =  open(arquivo, 'r')
    linhas = obras.readlines()
    for i in linhas:
        listar.ler_campos_do_arquivo()
        print(listar.__str__())
            
    tecla = input('Pressione ENTER para continuar')
    listar.fechar_arquivo()
    os.system('cls') or None
        
def op3():
    print   ('\t--Relatorio HTML--\t')
    tecla = input('Presione ENTER para continuar')
    os.system('cls') or None
    
    gravar = False
    arquivo = filedialog.askopenfilename(title='Escolher arquivo')
    relatorio = obra.Obra(gravar, arquivo)
    with open('obras.html', 'w') as pagina:
        
        pagina.write('<!DOCTYPE html>\n')
        pagina.write('<html lang="en">\n')
        pagina.write('<head>\n')
        pagina.write    ('\t<meta charset="UTF-8">\n')
        pagina.write    ('\t<meta name="viewport" content="width=device-width, inital-scale=1.0">\n')
        pagina.write    ('\t<title>Document</title>\n')
        pagina.write    ('\t<link rel="stylesheet" href="display.css">\n')
        pagina.write('</head>\n')
        pagina.write('<body>\n')
            
        pagina.write    ('\t<table>\n')
            
        pagina.write        ('\t\t<tr class="titulo">\n')
        pagina.write            ('\t\t\t<th colspan="6">RELATÓRIO DE OBRAS GALERIA VIRTUAL</th>\n')
        pagina.write        ('\t\t</tr>\n')

        pagina.write        ('\t\t<tr class="legenda">\n')
        pagina.write            ('\t\t\t<th>Ano/M~es</th>\n')
        pagina.write            ('\t\t\t<th>Nome</th>\n')
        pagina.write            ('\t\t\t<th>Estilo</th>\n')
        pagina.write            ('\t\t\t<th>Autor</th>\n')
        pagina.write            ('\t\t\t<th>Valor</th>\n')
        pagina.write            ('\t\t\t<th>Imagem</th>\n')
        pagina.write        ('\t\t</tr>\n')
            
        obras = open(arquivo, 'r')
        linhas = obras.readlines()
        for i in linhas:   
            relatorio.ler_campos_do_arquivo()
            pagina.write('\t\t<tr>\n')
            pagina.write    (f'\t\t\t<td>{relatorio.anoObra}/{relatorio.mesObra}</td>\n')
            pagina.write    (f'\t\t\t<td>{relatorio.nomeObra}</td>\n')    
            pagina.write    (f'\t\t\t<td>{relatorio.estiloObra}</td>\n')
            pagina.write    (f'\t\t\t<td>{relatorio.autorObra}</td>\n')
            pagina.write    (f'\t\t\t<td>{relatorio.valorObra}</td>\n')
            pagina.write    (f'\t\t\t<td><img src="{relatorio.urlObra}" alt=""></td>\n')
            pagina.write(f'\t\t</tr>\n')
            
        pagina.write    ('\t</table>\n')
            
        pagina.write('</body>\n')
        pagina.write('</html>\n')
        
    webbrowser.open("obras.html")
        
    tecla = input('Pressione ENTER para continuar')
    relatorio.fechar_arquivo()
    os.system('cls') or None
    
def op4():
    print('\t--Triangulo Pascal--\t')
    tecla = input('Pressione ENTER para continuar')
    os.system('cls') or None
    
    numeroBase = int(input('Digite o numero base que deseja:'))
    pascal = mat.Matematica(numeroBase)
    triangulo = pascal.triangulo_de_Pascal()
    os.system('cls') or None
    print('Seu Triângulo de Pascal:')
    for linha in triangulo:
        print(linha)
    tecla = input('\nPressione ENTER para continuar')

def seletor():
    escolha = 'x'
    while escolha != '0':
        print   ('\t--Galeria Virtuarte--\t')
        print   ('\n\nCadastro de obras de arte : 1')
        print   ('Listagem de obras de arte : 2')
        print   ('Página web de obras de arte : 3')
        print   ('Triângulo de Pascal : 4')
        print   ('\nTerminar : 0')
            
        escolha = input('\nDigite sua opção:')
        os.system('cls') or None
        match escolha:
            case    '1': op1()
            case    '2': op2()
            case    '3': op3()
            case    '4': op4()
    print('Obrigado por utilizar o programa!\n')
    print('Feito por Miguel Amorim e Pietro Amaral - 1° INFO')
    tecla = input('Pressione ENTER para continuar')

if __name__ == '__main__':
    os.system('cls') or None
    seletor()