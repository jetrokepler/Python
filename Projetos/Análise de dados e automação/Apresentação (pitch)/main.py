import pyautogui
import time
import pandas as pd
import pyperclip

tabela = pd.read_csv("Apresentação\Compras.csv", sep=";")

print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new"

pyautogui.hotkey("win","1") # atalho para abrir o Chrome na barra de tarefas.

time.sleep(3) # Fazendo esperar 6 segundos. 

pyautogui.write(url)

time.sleep(2)

pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=35, y=180) # Clicando em escrever.

time.sleep(4)

pyautogui.write("jetro.viana@aluno.ce.gov.br")

time.sleep(2)

pyautogui.press("tab") # Confirmar o destinatário.
pyautogui.press("tab") # Selecionar o assunto.

time.sleep(1)

pyperclip.copy("Relatório de compras.")

pyautogui.hotkey("ctrl","v") # O pyautogui não escreve caracteres com acento, por isso usa-se o pyperclip.

time.sleep(1)

pyautogui.press("tab") # Pular para o corpo do e-mail.

texto = f'''
Prezados,

segue o relatório de compras.

Total gasto: {total_gasto:,.2f}
Quantidade de produtos: {quantidade:,.2f}
Preço médio: {preco_medio:,.2f}
'''

time.sleep(1)


pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

time.sleep(1)

pyautogui.hotkey("ctrl","enter")

time.sleep(4)

print(pyautogui.position())