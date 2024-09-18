import pyautogui as pag
import keyboard

while True:
	x, y = pag.position()
	color = pag.pixel(x, y)
	print(color)
	if keyboard.is_pressed("q"):
		break