# 1 - Entendimento do desafio na área/empresa (Prever o preço de um barco baseado nas características dele);
# 2 - Importar da base dados;
# 3 - Ajuste na base de dados (no caso agora, não é necessário pois no print(tabela.ifo()) não houve erros);
# 4 - Análise exploratória (explorar as informações para descobrir a correlação entre as informações na base de dados);
# 5 - Modelagem + algoritmos (IA);
# 7 - Interpretação dos resultados.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # Seaborn e matplotlib para criar gráficos.
from sklearn.model_selection import train_test_split

tabela = pd.read_csv("barcos_ref.csv") # Importando a base de dados.

print(tabela)

correlacao = tabela.corr()[["Preco"]]

print(correlacao) # Pegando a correlação das informações.

# Mostrando a tabela dentro de um gráfico:

sns.heatmap(correlacao, cmap="Greens", annot=True) # Criando o gráfico, colocando um tema azul e colocando a valor da correlação nas barras.

plt.show() # Exibindo um gráfico.

# "y" é o que se quer prever, o objetivo, e "x" são os parâmetros para prever.

y = tabela["Preco"]
x = tabela.drop("Preco", axis=1) # Excluindo a coluna preco do "x".

# train test split (separando a tabela em uma parte de trino e em uma parte de teste)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)