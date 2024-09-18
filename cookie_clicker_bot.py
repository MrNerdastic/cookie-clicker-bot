import win32api
import win32con
import time
import pyautogui
import keyboard

go = False

time.sleep(3)
x, y = pyautogui.position()

def click(x, y, amount):
	win32api.SetCursorPos((x, y))
	for x in range(amount):
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def play():
	click(343, 483, 10000)


while True:
	if go:
		play()
	if keyboard.is_pressed("q"):
		if go:
			print("stop")
			go = False
		else:
			print("start")
			go = True
		time.sleep(1)
