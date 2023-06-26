from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import openai
import pickle

from gerador_de_pdf import PDF

servico = Service(ChromeDriverManager().install())

link = 'https://www.guiadacarreira.com.br/blog/conteudo-enem'

nome_arquivo = "OPENAI_API_KEY.pkl"

with open(nome_arquivo, "rb") as arquivo:
    openai_api_key = pickle.load(arquivo)

openai.api_key = openai_api_key

lista_de_seletores = [
'#__nuxt > div > main > div > div.article-page.z-mt-0800.z-mt-1400-desktop > section > div.z-mt-1000 > div.z-dynamic-content.article-page__content > div > ul:nth-child(30) > li:nth-child(19) > span',
'#__nuxt > div > main > div > div.article-page.z-mt-0800.z-mt-1400-desktop > section > div.z-mt-1000 > div.z-dynamic-content.article-page__content > div > ul:nth-child(30) > li:nth-child(22) > span',
'#__nuxt > div > main > div > div.article-page.z-mt-0800.z-mt-1400-desktop > section > div.z-mt-1000 > div.z-dynamic-content.article-page__content > div > ul:nth-child(30) > li:nth-child(35) > span'

]

pdf = PDF()

pdf.margens(20, 61, 20)
pdf.adicionar_pagina()

navegador = webdriver.Chrome(service = servico)
navegador.maximize_window()
navegador.get(link)

num_questao = 0

for seletor_css in lista_de_seletores:

    conteudo = navegador.find_element(By.CSS_SELECTOR, seletor_css).text

    elemento_para_scroll = navegador.find_element(By.CSS_SELECTOR, seletor_css)

    navegador.execute_script('arguments[0].scrollIntoView();', elemento_para_scroll)

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=[{"role": "user", "content": f"Faça uma questão com um enunciado de 10 linhas, com 5 alternativas com colchetes para marcar, com as alternativas separadas por parágrafos sendo apenas uma verdadeira, com uma letra maiúscula para representar cada alternativa e colchetes para marcar com caneta, sobre {conteudo} com uma explicação sobre qual a alternativa certa separada das alternativas por um parágrafo."}])
    questao = chat_completion['choices'][0]['message']['content']

    num_questao += 1

    pdf.adicionar_questoes(questao, num_questao)

pdf.salvar()

navegador.quit()