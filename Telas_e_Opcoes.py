# Tela Inicial

# Input de Informações
import os
from time import sleep
from Simulador import *
from Formalizado import *

msgInicial = 'Bem-vindo ao sistema de Financiamento Price (Modelo)'

msgOpcoes = '''===============
  01 - Simular Financiamento
  02 - Consultar Financiamento
  03 - Aprovar Financiamento
  00 - Sair
==============='''

msgRetorno = '''===============
  01 - Menu Inicial
  00 - Sair
==============='''

def retorno():
    print(msgRetorno)
    op = int(input())
    if op == 1:
        menuInicial()
    elif op == 0:
        sairSistema()
    else:
        print('Opção inválida!')
        retorno()

def sairSistema():
    print(' Obrigado por utilzar o sistema!\n Até logo.')
    sleep(2)
    exit()

def menuInicial():
    while True:
        os.system('cls')
        print(msgInicial)
        print(msgOpcoes)
        op = int(input())

        os.system('cls')
        match op:
            case 0:
                sairSistema()
            case 1: # Simular Financiamento
                caseSimularFinanc()
            case 2: # Consultar Financiamento
                print('===============')
                # Listar as simulações geradas
                for i, arquivos in enumerate(listaArquivos(pastaContratado())):
                    print('[{}] {}'.format(i,arquivos))
                print('===============')
                consultarContratado()
                retorno()
            case 3: # Aprovar Financiamento
                print('===============')
                # Listar as simulações aprovadas
                for i, arquivos in enumerate(listaArquivos(pastaSimulacao())):
                    print('[{}] {}'.format(i,arquivos))
                print('===============')
                nomeArquivo = consultarSimulacao()
                aprovarSimul(nomeArquivo)
                retorno()
            case _:
                print('Opção inválida!')
                sleep(1)

def caseSimularFinanc ():
    print('Executando Simulador de Financiamento')
    parametro, simulado = gerar_tabela()
    print('''===============
  01 - Corrigir parâmetros
  02 - Mostrar em tela
  03 - Gerar planilha
  04 - Menu inicial
  00 - Sair
===============''')
    op = int(input())
    match op:
        case 0:
            sairSistema()
        case 4:
            menuInicial()
        case 1:
            os.system('cls')
            caseSimularFinanc ()
        case 2:
            os.system('cls')
            print(
                f"Total de Parcelas: {parametro.loc[parametro['Parâmetro'] == 'Total de Parcelas','Valor'].values[0]:.2f}\n"+
                f"Total Financiado: {parametro.loc[parametro['Parâmetro'] == 'Total Financiado','Valor'].values[0]:.2f}\n"+
                f"Juros Anual (%): {parametro.loc[parametro['Parâmetro'] == 'Juros Anual (%)','Valor'].values[0]:.5f}\n"+
                f"Juros Mensal (%): {parametro.loc[parametro['Parâmetro'] == 'Juros Mensal (%)','Valor'].values[0]:.5f}\n"+
                f"Parcela Mínima: {parametro.loc[parametro['Parâmetro'] == 'Parcela Mínima','Valor'].values[0]:.2f}\n"
                )
            print('===============')
            print(simulado)
            print('''===============
  01 - Gerar Planilha
  02 - Nova Simulação
  03 - Menu Inicial
  00 - Sair
===============''')
            match int(input()):
                case 0:
                    sairSistema()
                case 1:
                    gerarArquivo(parametro, simulado)
                case 2:
                    os.system('cls')
                    caseSimularFinanc ()
                case 3:
                    menuInicial()
                case _:
                    print('Opção inválida!')
                    sleep(1)
        case 3:
            os.system('cls')
            print(
                f"Total de Parcelas: {parametro.loc[parametro['Parâmetro'] == 'Total de Parcelas','Valor'].values[0]:.2f}\n"+
                f"Total Financiado: {parametro.loc[parametro['Parâmetro'] == 'Total Financiado','Valor'].values[0]:.2f}\n"+
                f"Juros Anual (%): {parametro.loc[parametro['Parâmetro'] == 'Juros Anual (%)','Valor'].values[0]:.5f}\n"+
                f"Juros Mensal (%): {parametro.loc[parametro['Parâmetro'] == 'Juros Mensal (%)','Valor'].values[0]:.5f}\n"+
                f"Parcela Mínima: {parametro.loc[parametro['Parâmetro'] == 'Parcela Mínima','Valor'].values[0]:.2f}\n"
                )
            print('===============')
            print(simulado)
            print('===============')
            gerarArquivo(parametro, simulado)
            sleep(2)
        case _:
            print('Opção inválida!')
            sleep(1)

if __name__ == '__main__':
    menuInicial()