import os
import pandas as pd

# Consultar quais as Simulações confirmadas
def listaSimulacao():

    # Identificar se existe a pasta onde ficam as Simulações
    pastaDestino = 'Simulacao Gerada'
    if not os.path.exists(pastaDestino):
        print('Ainda não foi salvo nenhuma simulação')
    
    # Montar a lista de todas as simulações geradas
    arquivosExistentes = [
        f for f in os.listdir(pastaDestino)
        if f.endswith('.xlsx')
    ]

    # Listar as simulações geradas
    for i, arquivos in enumerate(arquivosExistentes):
        print('[{}] {}'.format(i,arquivos))

# Consultar os parâmetros da simulação selecionada

# Aprovar Simulações para Contratado
def aprovarSimul():
    pass
    # Transferir para a pasta de contratados
     

# Teste
if __name__ == '__main__':
    os.system('cls')
    print('===============')
    listaSimulacao()
    print('===============')


# Consultar Contratado Resumo

# Liquidação do Contratado

