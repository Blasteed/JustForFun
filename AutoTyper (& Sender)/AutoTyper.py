import time
import pyautogui
from termcolor import colored

print('\n\n')

print(colored("   AUTOTYPER BY KARFEE\n", 'magenta'))

text = input(colored("Text to send: ", 'yellow'))
emote = input(colored("Emote (click enter if you don't use it): ", 'yellow'))
repeats = input(colored("Times to repeat: ", 'yellow'))

print('\n\n')

print(colored(f"SENDING {text} {emote} FOR {repeats} TIMES\nWAITING 5 SECONDS TO START, GET READY !\n\n", 'blue'))

time.sleep(5)

print(colored("5 SECONDS PASSED, STARTING !\n\n", 'blue'))

for n in range(int(repeats)):
    pyautogui.write(f"{text} {emote}")
    pyautogui.press('return')

print(colored("PROCESS ENDED, KILLING !", 'blue'))

print('\n')