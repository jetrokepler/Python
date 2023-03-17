# 1 - Importar a base de dados;
# 2 - Visualizar a base de dados;
# 3 - Fazer o tratamento dos dados;
# 4 - Analisar a nota dos clientes;
# 5 - Como cada característica do cliente impacata na nota.

import pandas as pd
import plotly.express as px # Para fazer gráficos.

tabela = pd.read_csv("projeto 3\clientes.csv", encoding="latin", sep=";") # Usa-se o "encoding='latin'" para não dar erro por conta de caracteres especiais.

pd.set_option("display.max_columns", None)

# print(tabela.info()) Serve para ver as informações das colunas.

tabela = tabela.drop("Unnamed: 8", axis=1) # Deletando a coluna "Unnamed: 8" pois não há nada nela. Axis = 0 se for linha e axis = 1 se for coluna.

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce") # Corrigindo a coluna "Salário Anual (R$)" para transformá-la em número, e forçando o que não é número a tornar número.

# print(tabela[["Profissão"]].isna()) para ver as linhas vazias.

tabela = tabela.dropna() # Jogando fora informações vazias, pois não há como analisar um cliente se sua profissão estiver vazia.

print(tabela)

print("="*70)

print(tabela.describe()) # Entendendo as notas dos clientes.

# O "mean" significa média, e é o balizador, por exemplo, os clientes com nota maior que 53 são os que se procura.

for coluna in tabela.columns:

    grafico = px.histogram(tabela, x = coluna, y = "Nota (1-100)", histfunc = "avg", text_auto = True) # Criando o gráfico, colocando os números no gráfico e fazendo ele fazer uma média das notas.

    grafico.show()
    
# Perfil ideal de cliente:

# Idade > 15 anos (não tem muita diferença entre as faixas etárias depois disso);
# Faixa salarial não parece fazer muita diferença;
# Áreas de trabalho: Entretenimento e artista (Evitar construção);
# tem entre 10 e 15 anos de experiência;
# Com famílias não tão grandes (até no máx. 7 pessoas)