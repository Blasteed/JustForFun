import pyautogui as gui
from time import sleep


print ( '\n\nWaiting 10 seconds - Set your mouse pointer "AutoClick" position' )

sleep ( 10 )

print ( '\n\nStarting' )

print ( '\n' )


def AutoClick ():
    
    print ( 'Click\n' )
    
    gui.click ()
        
    print ( 'Waiting 1\n' )
    
    sleep ( 1 )
        
    AutoClick ()


AutoClick ()