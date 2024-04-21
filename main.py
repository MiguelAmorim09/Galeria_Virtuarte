import os
import obra
from tkinter import * 
from tkinter import filedialog    
import webbrowser
    
def op1():
    os.system('cls') or None
    print   ('\t--Cadastro de Obras--\t')
    tecla = input('Presione ENTER para continuar')
    
    os.system('cls') or None
    gravar = True
    arquivo = filedialog.askopenfilename(title='Escolher arquivo')
    cadastro = obra.Obra(gravar, arquivo)
    
    tecla   = input('Digite os dados da obra referente ao que e pedido\n\tPressione ENTER para continuar\t')
    ano     = input('Ano da obra:')
    mes     = input('Mes da obra:')
    autor   = input('Autor da obra:')
    nome    = input('Nome da obra:')
    estilo  = input('Estilo da obra:')
    valor   = input('Valor da obra:')
    url     = input('URL da obra:')
    
    cadastro.preencher_campos(ano, mes, autor, nome, estilo, valor, url)
    cadastro.gravar_campos_do_arquivo()
    
    input('Pressione ENTER para continuar')
    os.system('cls') or None
    
def op2():
    os.system('cls') or None
    print   ('\t--Listagem de obras--\t')
    tecla = input('Presione ENTER para continuar')
    os.system('cls') or None
    
    gravar = False
    arquivo = filedialog.askopenfilename(title='Escolher arquivo')
    cadastro = obra.Obra(gravar, arquivo)
    
    print('Ano\tMes\tAutor\t\t\tNome da Obra\t\t\tEstilo\t\t   Valor\tURL')
    with open(arquivo, 'r') as obras:
        linhas = obras.readlines()
        for i in linhas:
            cadastro.ler_campos_do_arquivo()
            print(cadastro.__str__())
            
    tecla = input('Pressione ENTER para continuar')
    os.system('cls') or None
        
def op3():
    os.system('cls') or None    
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
        pagina.write    ('\t<style>\n')
        pagina.write        ('\t\timg{\n')
        pagina.write            ('\t\t\twidth: 100px;\n')
        pagina.write            ('\t\t\theight: 100px\n')
        pagina.write        ('\t\t}\n')
        pagina.write        ('\t\ttable, th, td{\n')
        pagina.write            ('\t\t\tborder: 2px solid black;\n')
        pagina.write            ('\t\t\tborder-collapse: collapse;\n')
        pagina.write            ('\t\t\tpadding: 5px;\n')
        pagina.write        ('\t\t}\n')
        pagina.write        ('\t\t.titulo{\n')
        pagina.write            ('\t\t\tbackground-color: #20bfee;\n')
        pagina.write        ('\t\t}\n')
        pagina.write        ('\t\t.legenda{\n')
        pagina.write            ('\t\t\tbackground-color: #41cbd2;\n')
        pagina.write        ('\t\t}\n')
        pagina.write        ('\t\ttr:nth-child(2n+3){\n')
        pagina.write            ('\t\t\tbackground-color: #bce989;\n')
        pagina.write        ('\t\t}\n')
        pagina.write        ('\t\ttable{\n')
        pagina.write            ('\t\t\tmargin: auto;\n')
        pagina.write        ('\t\t}\n')
        pagina.write    ('\t</style>\n')
        pagina.write('</head>\n')
        pagina.write('<body>\n')
        
        pagina.write    ('\t<table>\n')
        
        pagina.write        ('\t\t<tr class="titulo">\n')
        pagina.write            ('\t\t\t<th colspan="6">RELATORIO DE OBRAS GALERIA VIRTUAL</th>\n')
        pagina.write        ('\t\t</tr>\n')

        pagina.write        ('\t\t<tr class="legenda">\n')
        pagina.write            ('\t\t\t<th>Ano/Mes</th>\n')
        pagina.write            ('\t\t\t<th>Nome</th>\n')
        pagina.write            ('\t\t\t<th>Estilo</th>\n')
        pagina.write            ('\t\t\t<th>Autor</th>\n')
        pagina.write            ('\t\t\t<th>Valor</th>\n')
        pagina.write            ('\t\t\t<th>Imagem</th>\n')
        pagina.write        ('\t\t</tr>\n')
        
        with open(arquivo, 'r') as obras:
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
    os.system('cls') or None
    
def op4():
    pass

def seletor():
    escolha = 'x'
    while escolha != '0':
        print   ('\t--Galeria Virtuarte--\t')
        print   ('\n\nCadastro de obras de arte : 1')
        print   ('Listagem de obras de arte : 2')
        print   ('Página web de obras de arte : 3')
        print   ('Triangulo de Pascal : 4')
        print   ('\nTerminar : 0')
            
        escolha = input('\nDigite sua opcao:')
        match escolha:
            case    '1': op1()
            case    '2': op2()
            case    '3': op3()
    print('Obrigado por utilizar o programa!')
    tecla = input('Pressione ENTER para continuar')

if __name__ == '__main__':
    os.system('cls') or None
    seletor()
    print('nada')