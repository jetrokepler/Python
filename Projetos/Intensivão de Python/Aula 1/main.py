# Passo a passo

# 1 - Importar base de dados;
# 2 - Calcular os indicadores;
# 3 - Enviar um e-mail.

import pyautogui # Biblioteca que meche no mouse e teclado.
import time # "Biblioteca do tempo".
import pandas as pd
import pyperclip

tabela = pd.read_csv("projeto 2\Compras.csv", sep=";") # "sep=';'" serve para separar a tabelas.

print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

# pyautogui.click -> clica;
# pyautogui.write -> escreve;
# pyautogui.press -> aperta uma tecla;
# pyautogui.hotkey -> aperta um atalho (ex. ctrl + C).
# pyautogui.scroll -> faz um scroll no mouse.

pyautogui.hotkey("win","1") # atalho para abrir o Chrome na barra de tarefas.

# pyautogui.PAUSE(1) Fazendo o programa pausar (pausa em todos os comandos).

pyautogui.hotkey("ctrl","t") # Atalho para abrir uma nova aba.

time.sleep(6) # Fazendo esperar 6 segundos.

# print(pyautogui.position()) Obtendo a posição do Gmail colocando o mouse encima quando o código rodar

pyautogui.click(x=611, y=142) # Clicando no Gmail (com a tela dividida, pela metade).

time.sleep(4)

pyautogui.click(x=34, y=210) # Clicando em escrever.

time.sleep(2)

pyautogui.click(x=414, y=455) # Clicando para escrever o destinatário.

time.sleep(3)

pyautogui.write("jetro.viana@aluno.ce.gov.br")

time.sleep(3)

pyautogui.press("tab") # Selecioonar o destinatário.

time.sleep(1)

pyautogui.press("tab") # Pular para o assunto.

time.sleep(3)

pyperclip.copy("Relatório de compras.")

pyautogui.hotkey("ctrl","v") # O pyautogui não escreve caracteres com acento, por isso usa-se o pyperclip.

time.sleep(3)

pyautogui.press("tab") # Pular para o corpo do e-mail.

texto = f'''
Prezados,

segue o relatório de compras.

Total gasto: {total_gasto:,.2f}
Quantidade de produtos: {quantidade:,.2f}
Preço médio: {preco_medio:,.2f}
'''
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

time.sleep(3)

pyautogui.hotkey("ctrl","enter")

time.sleep(6)

print(pyautogui.position())