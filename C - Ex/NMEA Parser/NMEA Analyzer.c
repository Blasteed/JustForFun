// YourKarfee - NMEA Sentences Slicer for School


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "NMEA.h"


int sNMEASatellitesNumb;
int sNMEATime;

double sNMEADiluition;
double sNMEALatitude;
double sNMEALongitude;

char sNMEALatitudeCard;
char sNMEALongitudeCard;

char sNMEAType[6];


void NMEAParser ()
{
    char NMEA_Sentence[100];

    int NMEA_Element_Index = 1;

    strcpy ( NMEA_Sentence, "$GPGGA,134658.00,5106.9792,N,11402.3003,W,2,09,1.0,1048.47,M,-16.27,M,08,AAAA*60" );

    char* sSentenceSlicer = strtok ( NMEA_Sentence, "," );

    sscanf ( sSentenceSlicer, "%s", sNMEAType );

    printf ( "%d:  %s\n", NMEA_Element_Index, sNMEAType );

    while ( sSentenceSlicer != NULL )
    {
        NMEA_Element_Index++;

        sSentenceSlicer = strtok ( NULL, "," );

        switch ( NMEA_Element_Index )
        {
            case TIME:

                sscanf ( sSentenceSlicer, "%d", &sNMEATime );

                printf ( "%d:  %d\n", NMEA_Element_Index, sNMEATime );

                break;

            case LATITUDE:

                sscanf ( sSentenceSlicer, "%lg", &sNMEALatitude );

                printf ( "%d:  %lg\n", NMEA_Element_Index, sNMEALatitude );

                break;

            case LATITUDE_DIR:

                sscanf ( sSentenceSlicer, "%c", &sNMEALatitudeCard );

                printf ( "%d:  %c\n", NMEA_Element_Index, sNMEALatitudeCard );

                break;

            case LONGITUDE:

                sscanf ( sSentenceSlicer, "%lg", &sNMEALongitude );

                printf ( "%d:  %lg\n", NMEA_Element_Index, sNMEALongitude );

                break;

            case LONGITUDE_DIR:

                sscanf ( sSentenceSlicer, "%c", &sNMEALongitudeCard );

                printf ( "%d:  %c\n", NMEA_Element_Index, sNMEALongitudeCard );

                break;

            case SATELLITES_NUMB:

                sscanf ( sSentenceSlicer, "%d", &sNMEASatellitesNumb );

                printf ( "%d:  %d\n", NMEA_Element_Index, sNMEASatellitesNumb );

                break;

            case DILUITION:

                sscanf ( sSentenceSlicer, "%lg", &sNMEADiluition );

                printf ( "%d:  %lg\n", NMEA_Element_Index, sNMEADiluition );

                break;

            default:

                break;
        }
    }
}
