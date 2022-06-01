import time
import pyautogui

print ( '\n\n' )

# Title's printing
print ( "   AUTOTYPER BY KARFEE\n" )


# End menu func
def EndMenu():

    # Menu choice input
    choice = input ( "\nChoose an option:\n\n1. Continue\n2. Exit\n\nChoice: " )

    # First choice, restarting
    if int ( choice ) == 1:

        print ( '\n' )

        Main ()

    # Second choice, exit
    elif int ( choice ) == 2:

        print ( '\n' )

        exit ()

    # Default choice
    else:

        print ( "\nERROR - CHOOSE A CORRECT OPTION\n" )

        EndMenu ()


# TextRep func
def TextRep():

    # Inputs of vars to run the code
    text = input ( "Text to send: " )

    repeats = int ( input ( "Times to repeat (int): " ) )

    # Var initialising
    spaces = "zero"

    # text input control
    if spaces != 'y' or spaces != 'n' or spaces != 'yes' or spaces != 'no' or spaces != 'Yes' or spaces != 'No' or spaces != 'YES' or spaces != 'NO' or spaces != 'Y' or spaces != 'N':

        spaces = input ( "Spaces between characters? (y/n): " )

    # Formatting
    print ( '\n' )

    # Var int casting
    if spaces == 'y' or spaces == 'Y' or spaces == 'yes' or spaces == "Yes" or spaces == "YES":

        spaces = int ( 1 )

        # Info printing
        print ( f"PRINTING {text} FOR {repeats} TIMES WITH SPACES" )

    # Inverse var cating
    else:

        spaces = int ( 0 )

        # Info printing
        print(f"PRINTING {text} FOR {repeats} TIMES WITHOUT SPACES")

    # Alert of delay before the starting
    print ( "WAITING 5 SECONDS TO START, GET READY !\n" )

    # Delay before starting
    time.sleep ( 5 )

    # Alert starting
    print ( "5 SECONDS PASSED, STARTING !\n" )

    # It repeats the printing, prints spaces if selected and sends at the end
    for n in range ( int ( repeats ) ):

        pyautogui.write ( f"{text}" )

        if spaces == 1:

            pyautogui.write ( " " )

        else:

            pass

    pyautogui.press ( 'return' )

    # Alert ending
    print( "PROCESS ENDED, KILLING !\n" )

    # Calling EndMenu
    EndMenu ()


# MessRep func
def MessRep():

    # Inputs of vars to run the code
    text = input ( "Text to send: " )

    repeats = int ( input ( "Times to repeat (int): " ) )

    delay = input ( "Delay's seconds between messages (int, Leave it empty if you don't use it): " )

    # Control of var to optimise printings
    if delay == '':

        delay = 0

    else:

        delay = int ( delay )

    # Formatting
    print ( '\n' )

    # Info printing
    print ( f"SENDING {text} FOR {repeats} TIMES WITH {delay}s OF DELAY" )

    # Alert of delay before the starting
    print ( "WAITING 5 SECONDS TO START, GET READY !\n" )

    # Delay before starting
    time.sleep ( 5 )

    # Alert starting
    print ( "5 SECONDS PASSED, STARTING !\n" )

    # It repeats the printing and the sending, respects the delay only if it exists and alert when it is using them
    for n in range ( int ( repeats ) ):

        pyautogui.write ( f"{text}" )

        if delay > 0:

            print ( f"RESPECTING {delay}s OF DELAY - {n + 1}\n" )

            time.sleep ( int ( delay ) )

        else:

            pass

        pyautogui.press ( 'return' )

    # Alert ending
    print( "PROCESS ENDED, KILLING !\n" )

    # Calling EndMenu
    EndMenu ()


# Main func
def Main():

    # Menu choice input
    choice = input ( "\nChoose an option:\n\n1. Text repetition (One message)\n2. Messages repetition\n\nChoice: " )

    # First choice, TextRep
    if int ( choice ) == 1:

        print ( '\nTEXT REPEATING\n' )

        TextRep ()

    # Second choice, MessRep
    elif int ( choice ) == 2:

        print ( '\nMESSAGE REPEATING\n' )

        MessRep ()

    # Default choice
    else:

        print ( "\nERROR - CHOOSE A CORRECT OPTION\n" )

        EndMenu ()


# First calling Main
Main()
