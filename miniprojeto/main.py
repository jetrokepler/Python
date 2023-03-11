# Lógica de programação.

# 1 - Importar a base de dados;
# 2 - Visuallizar a base de dados;
# 3 - Calcular o faturamento por loja;
# 4 - Calcular a quantidade de produtos vendidos por loja;
# 5 - Calcular o ticket médio por loja;
# 6 - Enviar um e-mail com o relatório.

# Instalação e importação das bibliotecas.

import pandas as pd
import win32com.client as win32

# Importando a base de dados.

tabela_vendas = pd.read_excel("Miniprojeto\Vendas.xlsx")

# Visualização da base de dados.

pd.set_option("display.max_columns", None) # Fazendo mostrar todas as colunas, O "None" quer dizer que não tem máximo de colunas, é pra mostrar todas.

# Cálculo de faturamento por loja.

faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum() # Filtrando para apenas duas colunas, agrupando "ID Loja" e somando o faturamento.

print(faturamento)

# Cálculo da quantidade de produtos vendidos por loja.

quantidade_produtos = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum() # Filtrando para apenas duas colunas, agrupando "ID Loja" e somando a quantidade.

print(quantidade_produtos)

# Cálculo de ticket médio.

ticket_medio = (faturamento["Valor Final"] / quantidade_produtos["Quantidade"]).to_frame() # Esse ".to_frame()" serve para que a divisão continue sendo uma tabela e não dê erro.

ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"}) # Renomeando a coluna.

print(ticket_medio)

# Enviar um e-mail com o relatório.

outlook = win32.Dispatch("outlook.application")
mail = outlook.CreateItem(0)
mail.To = "jetro.viana@aluno.ce.gov.br"
mail.Subject = "Relatório de vendas por loja."
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o relatório de vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={"Valor Final": "R${:,.2f}".format})}

<p>Quantidade de produtos vendidos:</p>
{quantidade_produtos.to_html()}

<p>Ticket médio dos pordutos em cada loja:</p>
{ticket_medio.to_html(formatters={"Ticket Médio": "R${:,.2f}".format})}

<p>Qualquer dúvida, estou às ordens.</>
<p>Atte.,</p>
<p>Jetro</p>
'''
# Esse ".to+html()" serve para trasnformar a tabela no e-mail, e o "formatters" serve para formatar os valores, no caso com cifrão, separador de milhar e decimal.

mail.Send()

print("e-mail enviado com sucesso.")