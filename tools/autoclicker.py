import pyautogui as pag
import keyboard
import time

go = False
while True:
	if go:
		pag.click()
	if keyboard.is_pressed("q"):
		if go:
			go = False
		else:
			go = True
		time.sleep(1)