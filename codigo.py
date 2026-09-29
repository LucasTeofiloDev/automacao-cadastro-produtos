

import getpass
import os
import time
from pathlib import Path

import pandas
import pyautogui

pyautogui.PAUSE = 0.5 # pausa de meio segundo entre os comandos
pyautogui.FAILSAFE = True
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
arquivo_produtos = Path(__file__).with_name("produtos.csv")

email = os.getenv("CADASTRO_EMAIL") or input("E-mail: ").strip()
senha = os.getenv("CADASTRO_SENHA") or getpass.getpass("Senha: ")

pyautogui.press('win') # abre a tela de pesquisa

pyautogui.write('chrome') # escreve o nome do sistema
pyautogui.press('enter') # abre o sistema

time.sleep(2)
pyautogui.hotkey("ctrl", "l")
pyautogui.write(link)
pyautogui.press('enter') # abre o link

time.sleep(3) # pyautogui hastag

pyautogui.click(x=-1179, y=373)
pyautogui.write(email) # escreve o usuario

pyautogui.press("tab")
pyautogui.write(senha)

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")


time.sleep(3) # pyautogui hastag

tabela = pandas.read_csv(arquivo_produtos)


for linha in tabela.index:
        
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=-1159, y=259) # clica no botão de cadastro
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) # escreve o nome do produto
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca)) # escreve a marca do produto
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo)) # escreve o tipo do produto
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]  
    pyautogui.write(str(categoria)) # escreve categoria do produto
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco"]
    pyautogui.write(str(preco)) # escreve a preço unitario do produto
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo)) # escreve a custo do produto
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]

    if pandas.notna(obs):
        pyautogui.write(str(obs))   

    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(500) # rola a tela para cima

