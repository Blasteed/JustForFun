// YourKarfee - NMEA Sentences Slicer for School

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TIME           2
#define LATITUDE       3
#define LATITUDE_DIR   4
#define LONGITUDE      5
#define LONGITUDE_DIR  6
#define DILUITION      9

char* NMEA_Time;
char* NMEA_Latitude;
char* NMEA_Latitude_Dir;
char* NMEA_Longitude;
char* NMEA_Longitude_Dir;
char* NMEA_Satellites_N;
char* NMEA_Diluition;

int main ()
{
    char NMEA_Sentence[100];

    int NMEA_Element_Index = 1;

    strcpy ( NMEA_Sentence, "$GPGGA,110617.00,41XX.XXXXX,N,00831.54761,W,1,05,2.68,129.0,M,50.1,M,,*42" );

    char* slicing = strtok ( NMEA_Sentence, "," );

    while ( slicing != NULL )
    {
        NMEA_Element_Index++;

        slicing = strtok ( NULL, "," );

        switch ( NMEA_Element_Index )
        {
            case TIME:

                NMEA_Time = slicing;

                for (  )
                {
                    if (  )
                }

                printf ( "NMEA_TIME:  %s\n", NMEA_Time );

                break;

            case LATITUDE:

                NMEA_Latitude = slicing;

                printf ( "NMEA_LATITUDE:  %s\n", NMEA_Latitude );

                break;

            case LATITUDE_DIR:

                NMEA_Latitude_Dir = slicing;

                printf ( "NMEA_LATITUDE_DIR:  %s\n", NMEA_Latitude_Dir );

                break;

            case LONGITUDE:

                NMEA_Longitude = slicing;

                printf ( "NMEA_LONGITUDE:  %s\n", NMEA_Longitude );

                break;

            case LONGITUDE_DIR:

                NMEA_Longitude_Dir = slicing;

                printf ( "NMEA_LONGITUDE_DIR:  %s\n", NMEA_Longitude_Dir );

                break;

            case DILUITION:

                NMEA_Diluition = slicing;

                printf ( "NMEA_DILUITION:  %s METERS\n", NMEA_Diluition );

                break;

            default:

                break;
        }
    }

    return 0;
}
