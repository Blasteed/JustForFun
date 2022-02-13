# SYSTEM MESSAGES: BLUE, SELECTIONS: YELLOW, TITLES: MAGENTA, ERRORS: RED

# imports: 1. termcolor to color terminal outputs, 2. os to control directories, 3. datetime to print dates on files
from termcolor import colored
import os
from datetime import datetime 

# colored title printing with \n formatting
print(colored('\n\n\n    FUNNYBASE (PYBASE) BY KARFEE    \n\n', 'magenta'))


#ENDMENU
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to call the end menu
def EndMenu():

    # end menu printing to choose mode with an else control (as switch case) to force you using only a right answer
    endmenu_choice = int(input('What do you want to do?\n\n'
                               '1. Exit\n'
                               '2. Continue\n\n' + # py chaining
                               colored('Choice?  ', 'yellow')))
    
    # \n formatting
    print('\n')
    
    # switch case simulating (NOT EXISTING IN PY)

    # "exit" selection
    if endmenu_choice == 1:
        
        # colored title printing with \n formatting
        print(colored("EXITING!\n\n", 'blue'))
        
        # calling exit built-in function to exit the program
        exit()
    
    # "continue" selection
    if endmenu_choice == 2:
        
        # colored title printing with \n formatting
        print(colored("STARTING AGAIN!\n\n", 'blue'))
        
        # re-calling the start menu to restart the program
        StartMenu()
        
    # default action
    else:
        
        # error printing for wrong answer used
        print(colored('ERROR - CHOOSE A RIGHT ANSWER!\n\n', 'red'))

        # restarting the start menu function
        EndMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#BASECREATE
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to create databases
def BaseCreate():
    
    # colored input to choose database's name with string casting 
    base_creating = str(input(colored("How will be this base named?  ", 'yellow')))
    
    # to transform the string in an all lowercase string
    base_creating = str.lower(base_creating)

    # colored input to choose database's columns' number with integer casting
    columns_creating = int(input(colored("How much columns will this base have?  ", 'yellow')))
    
    # creating and writing the base's name inside it and the date as first line, then closes it
    created_base = open(f'system_files\\{base_creating}.txt', 'w')
    created_base.write(f'{base_creating}.txt Database Created With FunnyBase at {datetime.now()}\n')
    created_base.close()

    # reopen the file to append
    created_base = open(f'system_files\\{base_creating}.txt', 'a')

    # it writes the number of columns as 'r' inside the second line of the file
    for columns in range(columns_creating):
        created_base.write("c")

    # goes on another line
    created_base.write('\n')

    # closes the file
    created_base.close()

    # reopen another time the file to append
    created_base = open(f'system_files\\{base_creating}.txt', 'a')

    # for the choosen number of columns, the program will ask their names, with colored output
    for columns in range(columns_creating):
        column_name = str(input(colored(f"What will be the name of the column number {columns + 1}?  ", 'yellow')))
        created_base.write(f"{column_name}\n")

    # closes the file
    created_base.close()
    
    # "database created" colored state printing with \n formatting
    print(colored(f"\n\nDATABASE '{base_creating}' WITH {columns_creating} COLUMNS CREATED!\n\n", 'blue'))

    # calling end menu
    EndMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#BASEREAD
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to read databases
def BaseRead():

    # print with \n formatting
    print(colored("Databases existing in the folder:\n", 'blue'))

    # repeats the operation for the number of files in the folder
    for files in os.listdir('system_files'):
        
        # it selects only files that ends with ".txt"
        if files.endswith(".txt"):
            
            # prints the name of files in the folder
            print(files)
            
    # base input selection with colored print
    base_selection = input(colored('\n\nChoice the database\'s name to read without ".txt"\n\n', 'blue') + # py chaining
                           colored("Choice:  ", 'yellow'))
    
    # to transform the string in an all lowercases string
    base_selection = str.lower(base_selection)
    
    # it controls if the files exists or not
    if os.path.isfile(f'system_files\\{base_selection}.txt') == False:
        
        # if file deosn't exist, it prints an error
        print(colored("\n\nERROR - BASE DOES NOT EXISTS! USE A CORRECT BASE'S NAME\n\n", 'red'))
        
        # it calls the function another time
        BaseRead()

    else:
        
        # if file exists it continues to run the code
        pass
        
    # \n formatting
    print('\n')

    # calling end menu
    EndMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#BASEMOD
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to modify databases
def BaseMod():

    # print with \n formatting
    print(colored("Databases existing in the folder:\n", 'blue'))

    # repeats the operation for the number of files in the folder
    for files in os.listdir('system_files'):
        
        # it selects only files that ends with ".txt"
        if files.endswith(".txt"):
            
            # prints the name of files in the folder
            print(files)
            
    # base input selection with colored print
    base_selection = input(colored('\n\nChoice the database\'s name to modify without ".txt"\n\n', 'blue') + # py chaining
                           colored("Choice:  ", 'yellow'))
    
    # to transform the string in an all lowercases string
    base_selection = str.lower(base_selection)
    
    # it controls if the files exists or not
    if os.path.isfile(f'system_files\\{base_selection}.txt') == False:
        
        # if file deosn't exist, it prints an error
        print(colored("\n\nERROR - BASE DOES NOT EXISTS! USE A CORRECT BASE'S NAME\n\n", 'red'))
        
        # it calls the function another time
        BaseMod()
        
    else:
        
        # if file exists it continues to run the code
        pass
        
    # \n formatting
    print('\n')

    # calling end menu
    EndMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#BASEDEL
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to delete databases
def BaseDel():

    # print with \n formatting
    print(colored("Databases existing in the folder:\n", 'blue'))
    
    # repeats the operation for the number of files in the folder
    for files in os.listdir('system_files'):
        
        # it selects only files that ends with ".txt"
        if files.endswith(".txt"):
            
            # prints the name of files in the folder
            print(files)
            
    # base input selection with colored print
    base_selection = input(colored('\n\nChoice the database\'s name to delete without ".txt"\n\n', 'blue') + # py chaining
                           colored("Choice:  ", 'yellow'))
    
    # to transform the string in an all lowercases string
    base_selection = str.lower(base_selection)
    
    # it controls if the files exists or not
    if os.path.isfile(f'system_files\\{base_selection}.txt') == False:
        
        # if file deosn't exist, it prints an error
        print(colored("\n\nERROR - BASE DOES NOT EXISTS! USE A CORRECT BASE'S NAME\n\n", 'red'))
        
        # it calls the function another time
        BaseDel()
    
    else:
        
        # if file exists it continues to run the code
        pass
    
    # it deletes the file user selected
    os.remove(f'system_files\\{base_selection}.txt')
    
    # after the deleting, it prints the name of the file deleted to control it
    print(colored(f"\n\nBASE {base_selection} REMOVED SUCCESSFULLY!", 'blue'))

    # \n formatting
    print('\n')

    # calling end menu
    EndMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#STARTMENU
# ----------------------------------------------------------------------------------------------------------------------------------------------
# a function to call the start menu in every moment
def StartMenu():

        # start menu printing to choose mode with an else control (as switch case) to force you using only a right answer
        startmenu_choice = int(input('What you want to do?\n\n'
                                '1. Create a new base\n'
                                '2. Read a base\n'
                                '3. Modify a base\n'
                                '4. Delete a base\n\n'+ # py chaining
                                colored('Choice?  ', 'yellow')))

        # \n formatting
        print('\n')

        # switch case simulating (NOT EXISTING IN PY)

        # "creating a new base" selection
        if startmenu_choice == 1:
            
            # colored title printing with \n formatting
            print(colored("    CREATING A NEW BASE!    \n\n", 'magenta'))

            # calling create function
            BaseCreate()

        # "reading" selection
        elif startmenu_choice == 2:
            
            # colored title printing with \n formatting
            print(colored("    READING A BASE!    \n\n", 'magenta'))

            # calling read function
            BaseRead()
        
        # "modifying a base" selection        
        elif startmenu_choice == 3:
            
            # colored title printing with \n formatting
            print(colored("    MODIFYING A BASE!    \n\n", 'magenta'))

            # calling modify function
            BaseMod()

        # "deleting a base" selection        
        elif startmenu_choice == 4:
            
            # colored title printing with \n formatting
            print(colored("    DELETING A BASE!    \n\n", 'magenta'))

            # calling delete function
            BaseDel()

        # default action
        else:

            # error printing for wrong answer used
            print(colored("ERROR - CHOOSE A RIGHT ANSWER!\n\n", 'red'))

            # restarting the function
            StartMenu()
# ----------------------------------------------------------------------------------------------------------------------------------------------


#MAIN
# ----------------------------------------------------------------------------------------------------------------------------------------------
# main function to recall it in a single script
def Main():

    # control if directory exists * if-1 *
    if os.path.isdir('system_files'):

        # control if base file exists * if-2 *
        if os.path.isfile('system_files\\start_base (DO NOT TOUCH ME).txt'):
        
            # if file exists, calling the start menu
            StartMenu()


        # closing * if-2 *
        else:
            
            # error colored printing
            print(colored("START BASE NOT EXISTING! CREATING\n\n", 'red'))

            # if not exists, creates the starting base and writes a line and the date to it and close it
            starting_base = open('system_files\\start_base (DO NOT TOUCH ME).txt', 'w')
            starting_base.write(f'exists! created at {datetime.now()}')
            starting_base.close()

            # state printing
            print(colored("START BASE CREATED! CALLING START MENU\n\n", 'blue'))

            # calling the start menu
            StartMenu()


    # closing * if-1 *
    else:
        
        # error colored printing
        print(colored("SYSTEM FOLDER NOT EXISTING! CREATING\n\n", 'red'))

        # if not exists create the functioning dir
        os.mkdir('system_files')

        # calling the start menu
        print(colored("SYSTEM DIR CREATED!\n\n", 'blue'))

        # main calling after creating system_dir
        Main()
# ----------------------------------------------------------------------------------------------------------------------------------------------

# main function calling
Main()