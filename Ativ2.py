import os

os.system('cls')

import pandas as pd


produto = ['Camiseta', 'Calça', 'Jaqueta', 'Vestido', 'Boné']
qtde = [50, 30, 15, 10, 25]

estoque = pd.Series(qtde, index=produto)
estoque.loc['Saia'] = None

print('PRODUTOS ACIMA DE 20 UNIDADES')
print()
print(estoque[estoque > 20])

preco_produto = pd.Series([3500, 2500, 1200, 900, 1500], index=produto)

total_estoque = estoque * preco_produto
print(50 * '=')
print('\nTOTAL EM ESTOQUE (R$)')
print()
print(total_estoque)