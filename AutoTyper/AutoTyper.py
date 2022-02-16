import time
import pyautogui
from termcolor import colored

print('\n\n')

print(colored("   AUTOTYPER BY KARFEE\n", 'magenta'))

text = input(colored("Text to send: ", 'yellow'))
repeats = input(colored("Times to repeat: ", 'yellow'))

print('\n')

print(colored(f'SENDING "{text}" FOR {repeats} TIMES\nWAITING 5 SECONDS TO START, GET READY !\n', 'blue'))

time.sleep(5)

print(colored("5 SECONDS PASSED, STARTING !\n", 'blue'))

for n in range(int(repeats)):
    pyautogui.write(f"{text}")
    pyautogui.press('return')

print(colored("PROCESS ENDED, KILLING !", 'blue'))

print('\n')