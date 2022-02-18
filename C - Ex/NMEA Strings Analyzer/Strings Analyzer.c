// YourKarfee - NMEA Sentences Slicer for School

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TYPE           1
#define TIME           2
#define LATITUDE       3
#define LATITUDE_DIR   4
#define LONGITUDE      5
#define LONGITUDE_DIR  6
#define CONTROL        7
#define SATELLITES     8
#define DILUITION      9
#define HEIGHT_ASL    10
#define HASL_UNIT     11
#define GEOIDE_HEIGHT 12
#define GH_UNIT       13
#define STATION_ID    14
#define CHECKSUM      15

char NMEA_Sentence[100];

char* NMEA_Type;
char* NMEA_Time;
char* NMEA_Latitude;
char* NMEA_Latitude_Dir;
char* NMEA_Longitude;
char* NMEA_Longitude_Dir;
char* NMEA_Diluition;

int main ()
{
    int NMEA_Element_Index = 1;

    strcpy ( NMEA_Sentence, "$GPGGA,110617.00,41XX.XXXXX,N,00831.54761,W,1,05,2.68,129.0,M,50.1,M,,*42" );

    char* slicing = strtok ( NMEA_Sentence, "," );

    NMEA_Type = slicing;

    while (slicing != NULL)
    {
        NMEA_Element_Index++;

        // printf ( "%s --- %d\n", slicing, strlen ( slicing ) );

        slicing = strtok ( NULL, "," );

        switch ( NMEA_Element_Index )
        {
            case TIME:

                NMEA_Time = slicing;

                break;

            case LATITUDE:

                NMEA_Latitude = slicing;

                break;

            case LATITUDE_DIR:

                NMEA_Latitude_Dir = slicing;

                break;

            case LONGITUDE:

                NMEA_Longitude = slicing;

                break;

            case LONGITUDE_DIR:

                NMEA_Longitude_Dir = slicing;

                break;

            case DILUITION:

                NMEA_Diluition = slicing;

                break;

            default:

                break;
        }
    }

    printf( "\n\nNMEA_TYPE:  %s\nNMEA_TIME:  %s\nNMEA_LATITUDE:  %s\nNMEA_LATITUDE_DIR:  %s\nNMEA_LONGITUDE:  %s\nNMEA_LONGITUDE_DIR:  %s\nNMEA_DILUITION:  %s\n", NMEA_Type, NMEA_Time, NMEA_Latitude, NMEA_Latitude_Dir, NMEA_Longitude, NMEA_Longitude_Dir, NMEA_Diluition );

    return 0;
}
