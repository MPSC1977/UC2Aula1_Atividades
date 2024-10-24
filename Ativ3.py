import os

os.system('cls')

import pandas as pd
import numpy as np


df = pd.read_excel('vendas_roupas.xlsx')
print(df.head(10))
print()

total_vendido = np.sum(df['Unidades Vendidas'])
print(50 * '=')
print('TOTAL DE PEÇAS VENDIDAS:')
print(total_vendido)
print()

media_preco = np.mean(df['Preço por Unidade (R$)'])
print(50 * '=')
print('PREÇO MÉDIO POR UNIDADE:')
print(media_preco)
print()

maior_fat = np.max(df['Faturamento Total (R$)'])
print(50 * '=')
print('PRODUTO COM MAIOR FATURAMENTO TOTAL:')
print(maior_fat)
print()

menor_fat = np.min(df['Faturamento Total (R$)'])
print(50 * '=')
print('PRODUTO COM MENOR FATURAMENTO TOTAL:')
print(menor_fat)
print()

baixa_satisfacao = df['Satisfação']
print(50 * '=')
print('PRODUTOS COM BAIXO NÍVEL DE SATISFAÇÃO:')
print(baixa_satisfacao)
