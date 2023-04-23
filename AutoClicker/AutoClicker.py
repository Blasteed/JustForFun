import pyautogui as gui
from time import sleep


rep = 0

rep_verify = 0


rep = int ( input ( '\n\nSet a number of click repetitions: ' ) )

print ( '\n\nWaiting 10 seconds - Set your mouse pointer "AutoClick" position' )

sleep ( 10 )

print ( '\n\nStarting' )

print ( '\n' )


def AutoClick ( rep_verify, rep ):
    
    if rep_verify == rep:
        
        print ( '\nRepetitions\' number reached\n\nWaiting 10 then exiting\n\n' )
        
        sleep ( 10 )
         
        exit ()
        
    else:
    
        print ( 'Click\n' )
    
        gui.click ()
        
        print ( f'{ rep_verify + 1 } out of { rep } - Waiting 3 then verifying\n' )
    
        sleep ( 3 )
    
        rep_verify += 1
        
        AutoClick ( rep_verify, rep )


AutoClick ( rep_verify, rep )