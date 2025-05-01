### Calc_FinancPrice

### Importar bibliotecas
import os
import pandas as pd
from datetime import datetime

### Calcular parcelas
def gerar_tabela():

    print('===============')
    quantiaParcela = int(input ('Número de parcelas:'))
    valorFinanciamento = float(input('Valor que foi financiado:'))
    jurosAnual = float(input('Percentual de juros definido por ano:'))
    taxaJuros = ((1+jurosAnual/100) ** (1/12))-1
    parcelaCalculada = valorFinanciamento * (taxaJuros * (1 + taxaJuros) ** quantiaParcela) / ((1 + taxaJuros) ** quantiaParcela - 1)

    saldoDevedor = valorFinanciamento
    
    parametros = pd.DataFrame({
        'Parâmetro': ['Total de Parcelas','Total Financiado','Juros Anual (%)','Juros Mensal (%)','Parcela Mínima'],
        'Valor': [int(quantiaParcela), round(valorFinanciamento,2), jurosAnual, taxaJuros, round(parcelaCalculada,2)]
    })

    linhas = []
    
    for parcela in range(0,quantiaParcela + 1):
        if parcela == 0:
            linhas.append([
                parcela,
                0,
                0,
                0,
                saldoDevedor
            ])
        else:
            valorJuros = saldoDevedor * taxaJuros
            valorAmortizacao = parcelaCalculada - valorJuros
            saldoDevedor = max(0,saldoDevedor + valorJuros - parcelaCalculada)
            linhas.append([
                parcela,
                round(parcelaCalculada,2),
                round(valorAmortizacao,2),
                round(valorJuros,2),
                round(saldoDevedor,2)
            ])
    tabela = pd.DataFrame(linhas,columns=["Parcela","Valor Parcela","Amortização","Juros","Saldo Devedor"])
    return parametros, tabela

def gerarArquivo (parametros, tabela):
    hoje = datetime.now().strftime('%Y%m%d')
    pastaDestino = 'Simulacao Gerada'

    # Verificar e gerar pasteDestino caso não exista
    if not os.path.exists(pastaDestino):
        os.makedirs(pastaDestino)

    # Contar arquivos existentes na pasta
    arquivosExistentes = [
        f for f in os.listdir(pastaDestino)
        if f.endswith('.xlsx')
    ]
    contagem = len(arquivosExistentes) + 1
    nomeArquivo = f'{hoje}_{contagem:03}.xlsx'

    destinoArquivo = os.path.join(pastaDestino, nomeArquivo)

    with pd.ExcelWriter(destinoArquivo, engine='openpyxl') as writer:
        parametros.to_excel(writer, index=False, sheet_name = 'Parametros')
        tabela.to_excel(writer, index=False, sheet_name = 'Simulacao')
    
    print(f' Arquivo {destinoArquivo} salvo!\n Caminho:{destinoArquivo}')

# Retorno da tabela finaliza
if __name__ == '__main__':
    parametro, tabela = gerar_tabela()
    gerarArquivo(parametro, tabela)

