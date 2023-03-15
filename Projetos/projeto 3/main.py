# 1 - Importar a base de dados;
# 2 - Visualizar a base de dados;
# 3 - Fazer o tratamento dos dados;
# 4 - Analisar a nota dos clientes;
# 5 - Como cada característica do cliente impacata na nota.

import pandas as pd

tabela = pd.read_csv("Projetos\projeto 3\clientes.csv", encoding="latin", sep=";") # Usa-se o "encoding='latin'" para não dar erro por conta de caracteres especiais.

tabela = tabela.drop("Unnamed: 8", axis=1) # Deletando a coluna "Unnamed: 8" pois não há nada nela. Axis = 0 se for linha e axis = 1 se for coluna.

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce") # Corrigindo a coluna "Salário Anual (R$)" para transformá-la em número, e forçando o que não é número a tornar número.

print(tabela)

print(tabela.info()) # Serve para ver as informações das colunas.

# Corrigir informações vazias (imaginando que um cliente não tem sua profissão e sua nota na tabela. Não tem como considerar ele, então tem que corrigir).