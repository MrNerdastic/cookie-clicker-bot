from pynput.mouse import Button, Controller
import time
import keyboard

mouse = Controller()
go = False
while True:
	if go:
		mouse.click(Button.left, 1)
	if keyboard.is_pressed("q"):
		if go:
			print("stop")
			go = False
		else:
			print("start")
			go = True
		time.sleep(1)