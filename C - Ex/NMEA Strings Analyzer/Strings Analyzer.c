// YourKarfee - NMEA Sentences Slicer for School

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* NMEA_Sentence = "$GPGGA,110617.00,41XX.XXXXX,N,00831.54761,W,1,05,2.68,129.0,M,50.1,M,,*42";

char NMEA_Type[6];
char NMEA_Time[6];
char NMEA_Latitude[11];
char NMEA_Latitude_Dir[1];
char NMEA_Longitude[11];
char NMEA_Longitude_Dir[1];
char NMEA_Diluition[4];

int main ()
{
    strncpy ( NMEA_Type, &NMEA_Sentence[0], 6 );
    strncpy ( NMEA_Time, &NMEA_Sentence[7], 6 );
    strncpy ( NMEA_Latitude, &NMEA_Sentence[17], 10 );
    strncpy ( NMEA_Latitude_Dir, &NMEA_Sentence[28], 1 );
    strncpy ( NMEA_Longitude, &NMEA_Sentence[30], 11 );
    strncpy ( NMEA_Longitude_Dir, &NMEA_Sentence[42], 1 );
    strncpy ( NMEA_Diluition, &NMEA_Sentence[49], 4 );

    printf( "\n\nNMEA_TYPE:  %s\nNMEA_TIME:  %s\nNMEA_LATITUDE:  %s\nNMEA_LATITUDE_DIR:  %s\nNMEA_LONGITUDE:  %s\nNMEA_LONGITUDE_DIR:  %s\nNMEA_DILUITION:  %s\n", NMEA_Type, NMEA_Time, NMEA_Latitude, NMEA_Latitude_Dir, NMEA_Longitude, NMEA_Longitude_Dir, NMEA_Diluition );
}
