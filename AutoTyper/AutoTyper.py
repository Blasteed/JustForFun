import time
import pyautogui
from termcolor import colored

print('\n\n')

# Title's colored printing
print(colored("   AUTOTYPER BY KARFEE\n", 'magenta'))


# End menu func
def EndMenu():

    # Menu choice with colored print
    choice = int(input("Choose an option:\n\n1. Continue\n2. Exit\n\n" + colored("Choice: ", 'yellow')))

    # First choice, restarting
    if choice == 1:
        print('\n')
        Main()

    # Second choice, exit
    if choice == 2:
        print('\n')
        exit()

    # Default choice
    else:
        print(colored("\nERROR - CHOOSE A CORRECT OPTION\n", 'red'))
        EndMenu()


# Main func
def Main():

    # Colored inputs of vars to run the code
    text = input(colored("Text to send: ", 'yellow'))
    repeats = int(input(colored("Times to repeat (int): ", 'yellow')))
    delay = input(colored("Delay's seconds between messages (int, Leave it empty if you don't use it): ", 'yellow'))

    # Control of var to optimise printings
    if delay == '':
        delay = 0
    else:
        delay = int(delay)

    print('\n')

    # Info printing
    print(colored(f"SENDING {text} FOR {repeats} TIMES WITH {delay}s OF DELAY", 'blue'))

    # Alert of delay before the starting
    print(colored('WAITING 5 SECONDS TO START, GET READY !\n', 'blue'))

    # Delay before starting
    time.sleep(5)

    # Alert starting
    print(colored("5 SECONDS PASSED, STARTING !\n", 'blue'))

    # It repeats the printing and the sending, respects the delay only if it exists and alert when it is using them
    for n in range(int(repeats)):

        pyautogui.write(f"{text}")

        if delay > 0:
            print(colored(f"RESPECTING {delay}s OF DELAY - {n + 1}\n", 'blue'))
            time.sleep(int(delay))
        else:
            pass

        pyautogui.press('return')

    # Alert ending
    print(colored("PROCESS ENDED, KILLING !\n", 'blue'))

    # Calling EndMenu
    EndMenu()


# First calling Main
Main()
