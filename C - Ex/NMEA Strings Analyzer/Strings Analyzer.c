#include <stdio.h>
#include <string.h>

int i = 0;

char string_to_analyze[100] = "";

char NMEA_Type[6] = "";
char NMEA_Time[6] = "";
char NMEA_Latitude[10] = "";
char NMEA_Longitude[10] = "";
char NMEA_Diluition[4] = "";

int iForStart = 0;
int iForStop = 5;

int main ()
{
    printf ( "\n\n\nInserire stringa NEO-6 NMEA da Analizzare:  " );
    scanf ( "%s", string_to_analyze );

    printf ( "\n\nLa stringa NEO-6 NMEA che hai inserito corrisponde a:  %s", string_to_analyze );

    for ( i = 0; i >= strlen(string_to_analyze); i++ )
    {
        NMEA_Type[i] = string_to_analyze[i];

        if ( NMEA_Type[6] != "" )
        {
            NMEA_Time[i] = string_to_analyze[i];
        }

        if ( NMEA_Time[6] != "" )
        {
            NMEA_Latitude[i] = string_to_analyze[i];
        }

        if ( NMEA_Longitude[10] != "" )
        {
            NMEA_Longitude[i] = string_to_analyze[i];
        }

        if ( NMEA_Latitude[10] != "" )
        {
            NMEA_Diluition[i] = string_to_analyze[i];
        }
    }

    printf( "\n\nNMEA_TYPE:  %s\nNMEA_TIME:  %s\nNMEA_LATITUDE:  %s\nNMEA_LONGITUDE:  %s\nNMEA_DILUITION:  %s\n", NMEA_Type, NMEA_Time, NMEA_Latitude, NMEA_Longitude, NMEA_Diluition );
}



