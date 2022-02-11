import time
import pyautogui

print('\n\n')

text = input('text: ')
repeat = input("number of times: ")

time.sleep(3)

for n in range(int(repeat)):
    pyautogui.write(str(text))
    pyautogui.press('return')