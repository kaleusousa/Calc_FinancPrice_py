import os
import pandas as pd
import shutil

def pastaSimulacao():
    pasta = 'Simulacao Gerada'
    return pasta

def pastaContratado():
    pasta = 'Contratado'
    return pasta

# Consultar arquivos
def listaArquivos(pasta):

    # Montar a lista de todos os arquivos presentes na pasta
    arquivosExistentes = [
        f for f in os.listdir(pasta)
        if f.endswith('.xlsx') and not f.startswith('~$')
    ]

    return arquivosExistentes

# Consultar os parâmetros da simulação selecionada
def consultarSimulacao():
    pastaDestino = pastaSimulacao()
    lista = listaArquivos(pastaDestino)
    op = int(input())
    nomeArquivo = lista[op]

    caminho = os.path.join(pastaDestino,nomeArquivo)

    planilha = pd.read_excel(caminho,sheet_name='Parametros')
    print(planilha)
    return nomeArquivo

# Aprovar Simulações para Contratado
def aprovarSimul(nomeArquivo):
    # Verificar e gerar pasteDestino caso não exista
    if not os.path.exists((pastaContratado())):
        os.makedirs(pastaContratado())
    
    # Transferir para a pasta de contratados
    origem = os.path.join(pastaSimulacao(),nomeArquivo)
    destino = os.path.join(pastaContratado(),nomeArquivo)

    shutil.move(origem,destino)

# Consultar Contratado Resumo
def consultarContratado():
    pastaDestino = pastaContratado()
    lista = listaArquivos(pastaDestino)
    op = int(input())
    nomeArquivo = lista[op]

    caminho = os.path.join(pastaDestino,nomeArquivo)

    resumo = pd.read_excel(caminho,sheet_name='Parametros')
    planilha = pd.read_excel(caminho,sheet_name='Simulacao')
    print(resumo)
    print('===============')
    print(planilha)
    return nomeArquivo

# Teste
if __name__ == '__main__':
    os.system('cls')
    print('===============')
    # Listar as simulações geradas
    for i, arquivos in enumerate(listaArquivos(pastaContratado())):
        print('[{}] {}'.format(i,arquivos))
    print('===============')
    nomeArquivo = consultarContratado()
