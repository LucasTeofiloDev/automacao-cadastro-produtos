"""Mostra a posição do mouse para calibrar as coordenadas da automação."""

import time

import pyautogui


print("Posicione o mouse no campo desejado. A leitura será feita em 3 segundos.")
time.sleep(3)
print(pyautogui.position())
