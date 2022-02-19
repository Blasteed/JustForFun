// YourKarfee - NMEA Sentences Slicer for School

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "NMEA.h"

char* sNMEATime;
char* sNMEALatitude;
char* sNMEALatitudeCard;
char* sNMEALongitude;
char* sNMEALongitudeCard;
char* sNMEASatellitesNumb;
char* sNMEADiluition;

void Parser ()
{
    char NMEA_Sentence[100];

    int NMEA_Element_Index = 1;

    strcpy ( NMEA_Sentence, "$GPGGA,110617.00,41XX.XXXXX,N,00831.54761,W,1,05,2.68,129.0,M,50.1,M,,*42" );

    char* sSentenceSlicer = strtok ( NMEA_Sentence, "," );

    while ( sSentenceSlicer != NULL )
    {
        NMEA_Element_Index++;

        sSentenceSlicer = strtok ( NULL, "," );

        switch ( NMEA_Element_Index )
        {
            case TIME:

                sNMEATime = sSentenceSlicer;

                printf ( "TIME:  %s\n", sNMEATime );

                break;

            case LATITUDE:

                sNMEALatitude = sSentenceSlicer;

                printf ( "LATITUDE:   %s\n", sNMEALatitude );

                break;

            case LATITUDE_DIR:

                sNMEALatitudeCard = sSentenceSlicer;

                printf ( "CARD_LATITUDE:   %s\n", sNMEALatitudeCard );

                break;

            case LONGITUDE:

                sNMEALongitude = sSentenceSlicer;

                printf ( "LONGITUDE:  %s\n", sNMEALongitude );

                break;

            case LONGITUDE_DIR:

                sNMEALongitudeCard = sSentenceSlicer;

                printf ( "CARD_LONGITUDE:  %s\n", sNMEALongitudeCard );

                break;

            case SATELLITES_NUMB:

                sNMEASatellitesNumb = sSentenceSlicer;

                printf ( "SATELLITES_NUMB:  %s\n", sNMEASatellitesNumb );

                break;

            case DILUITION:

                sNMEADiluition = sSentenceSlicer;

                printf ( "DILUITION:  %s METERS\n", sNMEADiluition );

                break;

            default:

                break;
        }
    }
}
