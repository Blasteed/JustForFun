import time
import pyautogui

text = input('text: ')
repeat = input("number of times: ")

time.sleep(3)

for n in range(int(repeat)):
    pyautogui.write(str(text))
    #time.sleep(0.2)
    pyautogui.press('return')
    #time.sleep(0.2)