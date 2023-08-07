import requests
import json
from termcolor import colored # Used for colored printing, installation required and recommended
from time import sleep



Octo_Addr = '127.0.0.1' # Localhost, Loopback address
Octo_API_Key = ''



def Listening ( Printer_State, Available_Port ):

    if Printer_State == "Operational": # Control connection status and, if Connected, resatrt GET Request

        print ( "\n\nPrinter State: ", colored ( Printer_State, 'green' ), "\n\n\nRestarting GET Request in 3 secs\n\n\n" )

        sleep ( 3 )

        GET_Request ( )

    elif Printer_State == "Closed": # If printers is not connected, it controls USB Serial connection availability and, if available, tries to connect. If not available, restart GET

        if len ( Available_Port ) == 0:

            print ( "\n\nPrinter State: ", colored ( Printer_State, 'red' ) )

            print ( f"\n\nNumber of available ports is: { colored ( len ( Available_Port ), 'red' ) }\n\n\nRestarting GET Request in 3 secs\n\n\n" )

            sleep ( 3 )

            GET_Request ( )

        else:

            print ( "\n\nPrinter State: ", colored ( Printer_State, 'red' ) )

            print ( f"\n\nNumber of available ports is: { colored ( len ( Available_Port ), 'green' ) }\n\n\nAttempting Connection in 5 secs\n\n\n" )

            sleep ( 3 )

            print ( "\n\nPorts: ", colored ( Available_Port [0], 'blue' ), '\n\n' )



            Connection_Handle_APIPayload = \ # Payload attributes to send with POST request. Needed to start the connection
            {
                "command" : "connect",
                "port" : Available_Port [0],
                "autoconnect" : 'true'
            }

            Connection_Handle_APIReq = f"http://{ Octo_Addr }/api/connection?apikey={ Octo_API_Key }"

            print ( colored ( "\n\n---- CONNECTING ----", 'cyan' ) )

            API_POST_Response = requests.post ( Connection_Handle_APIReq, json = Connection_Handle_APIPayload )



            if API_POST_Response.status_code == 204: # Code 204 is the "OK Code", 400 is "Error Code". Script controls if the USB is connected or not

                print ( colored ( f"\n\n\nConnected to { Available_Port [0] }", 'green' ) )

                print ( "\n\n\nRestarting GET Request in 3 secs\n\n\n" )

                sleep ( 3 )

                GET_Request ( )

            else:

                print ( '\n\n\n', colored ( API_POST_Response, 'yellow' ), '\n\nError occurred\n\n\nRestarting GET Request in 3 secs\n\n\n' )

                sleep ( 3 )

                GET_Request ( )



def GET_Request (): # Get Request used to collect Printer's connection informations

    API_GET_Response = requests.get ( f"http://{ Octo_Addr }/api/connection?apikey={ Octo_API_Key }" )



    if API_GET_Response.status_code == 200: # Error check, if 200 API is reachable. Else, if GET response is 404 Code, it is no longer available

        print ( "\n\nResponse Code: ", colored ( "200", 'green' ) )



        JSON_RawKeys = json.dumps ( API_GET_Response.json (), indent=4, sort_keys=True )

        JSON_Keys = json.loads ( JSON_RawKeys )

        Available_Port = JSON_Keys [ 'options' ][ 'ports' ]

        Printer_State = JSON_Keys [ 'current' ][ 'state' ]



        Listening ( Printer_State, Available_Port )

    elif API_GET_Response.status_code == 404:

        print ( "\n\nResponse Code: ", colored ( f"Error { API_GET_Response.status_code } on 1st API GET Request\n", 'red' ), "\n\nRestarting GET Request in 3 secs\n\n" )

        sleep ( 3 )

        GET_Request ( )



GET_Request ( ) # Script's "Main" Function Recall
