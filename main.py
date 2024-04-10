import os
from tkinter import*
import obra

def seletor() -> str:
    print('--Galeria Virtuarte--')
    input('Pressione ENTER para continuar')
    
    print('\n\nCadastrar obra : 1')
    
    print('\nTerminar : 0')
    
    escolha = input('\nDigite a opcao desejada:')
    os.system('cls') or None
    return escolha

def realizar(opcaoDesejada:str):
    def op1():
        print('--Cadastro de Obras--')
        input('Pressione ENTER para continuar')
        ano = input('Insira o ano da obra:')
        mes = input('Insira o mes da obra:')
        autor = input('Insira o nome do autor da obra:')
        nome = input('Insira o nome da obra:')
        estilo = input('Insira o estilo da obra:')
        valor = input('Insira o valor estimado da obra:')
        url = input('Insira a url de uma foto da obra:')
        aberto = True
        nomeArquivo = 'obras.txt'
        cadastro = obra.Obra(ano, mes, autor, nome, estilo, valor, url, aberto, nomeArquivo)
        cadastro.gravarCamposNoArquivo()
        
    match opcaoDesejada:
        case    '1': op1()
        
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