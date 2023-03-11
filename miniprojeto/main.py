# Lógica de programação.

# 1 - Importar a base de dados;
# 2 - Visuallizar a base de dados;
# 3 - Calcular o faturamento por loja;
# 4 - Calcular a quantidade de produtos vendidos por loja;
# 5 - Calcular o ticket médio por loja;
# 6 - Enviar um e-mail com o relatório.

# Instalação e importação das bibliotecas.

import pandas as pd

# Importando a base de dados.

tabela_vendas = pd.read_excel("Miniprojeto\Vendas.xlsx")

print(tabela_vendas)