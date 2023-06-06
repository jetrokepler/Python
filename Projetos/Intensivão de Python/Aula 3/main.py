# 1 - Abrir o navegador;
# 2 - Importar a base de dados;
# 3 - Pesquisar o prçe atual de cada produto da base de dados;
# 4 - Atualizar o preo atual na base de dados;
# 5 - Decidir quais produtos comprar.

import pandas as pd
from selenium import webdriver # A vantagem de importar a penas o webdriver e não todo o selenium é fazer o código ficar mais leve. O selenium, diferente do pyautogui, faz o código rodar em sugundo plano, e outra vantagem é que ele sabe a hora de funcionar, ou seja, ele reconhece a hora que uma aba está abrindo, por exemplo.

tabela = pd.read_excel("projeto 4\commodities.xlsx")

navegador = webdriver.Chrome() # Abrindo o navegador.

for linha in tabela.index: # O python só reconhece "linha" por causa que "tabela.index" é uma lista que tem todas as linhas da tabela. O "for" está sendo utilizado para que, em cada linha da coluna "Produto", seja encontrado o preço atual do produto no site informado. 

    produto = tabela.loc[linha, "Produto"] # Localizando uma célula da tabela de acordo com sua linha e sua coluna

    print(produto)

    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace("ç", "c").replace("ú", "u").replace("é", "e")

    link = f"https://www.melhorcambio.com/{produto}-hoje"

    navegador.get(link) # Seleciona o site.

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute("value") # Procurando um elemento na página e pegando um valor, no caso, o do preço.

    # .click() serve para clicar;
    # .send_keys("texto") para escrever;
    # .get_atribute() para pegar um valor.

    preco = preco.replace(".", "").replace(",", ".") # Colocando no formato americano.

    tabela.loc[linha, "Preço Atual"] = float(preco) # Fazendo a coluna "Preço Atual" da tabela receber os valores. O "float" foi usado para que a tablea receba um número e não uma string.

    print(preco)

tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]

print(tabela)

tabela.to_excel("projeto 4\commodities_atualizado.xlsx", index = False) # Criando a tabela atualizada e excluindo a coluna de índice.