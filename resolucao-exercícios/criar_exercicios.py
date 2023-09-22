import pyautogui as pag
from time import sleep

cont = 0
i = 32
sleep(3)

while cont <= 8:
	pag.hotkey('ctrl', 'c')
	pag.hotkey('ctrl', 'v')
	sleep(0.5)
	pag.press('f2')
	sleep(0.5)
	pag.write('ex0' + str(i + cont))
	sleep(0.5)
	pag.press('enter')
	cont += 1