import win32api
import win32con
import time
import pyautogui
import keyboard

time.sleep(3)
x, y = pyautogui.position()

def click():
    # Move the cursor to the position (x, y)
    win32api.SetCursorPos((x, y))
    
    # Perform left mouse button down and up actions to simulate a click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

go = False
while True:
	if go:
		click()
	if keyboard.is_pressed("q"):
		if go:
			print("stop")
			go = False
		else:
			print("start")
			go = True
		time.sleep(1)
