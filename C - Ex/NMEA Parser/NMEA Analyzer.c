// YourKarfee - NMEA Sentences Slicer for School

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "NMEA.h"


int iNMEASatellitesNumb = 0;

float fNMEADiluition = 0;

double dNMEALatitude  = 0;
double dNMEALongitude = 0;

char cNMEALatitudeCard;
char cNMEALongitudeCard;

char sNMEAType[6] = "";
char sNMEATime[6] = "";


void NMEA_Parser ()
{
    char sNMEASentence[100];

    int imNMEAElementIndex = 1;

    strcpy ( sNMEASentence, "$GPGGA,001038.00,3334.2313457,N,11211.0576940,W,2,04,5.4,354.682,M,- 26.574,M,7.0,0138*79" );

    char* psSentenceSlicer = strtok ( sNMEASentence, "," );

    sscanf ( psSentenceSlicer, "%s", sNMEAType );

    while ( psSentenceSlicer != NULL && imNMEAElementIndex < DILUITION )
    {
        imNMEAElementIndex++;

        psSentenceSlicer = strtok ( NULL, "," );

        switch ( imNMEAElementIndex )
        {
            case TIME:

                sscanf ( psSentenceSlicer, "%s", sNMEATime );

                break;

            case LATITUDE:

                sscanf ( psSentenceSlicer, "%lg", &dNMEALatitude );

                break;

            case LATITUDE_DIR:

                sscanf ( psSentenceSlicer, "%c", &cNMEALatitudeCard );

                break;

            case LONGITUDE:

                sscanf ( psSentenceSlicer, "%lg", &dNMEALongitude );

                break;

            case LONGITUDE_DIR:

                sscanf ( psSentenceSlicer, "%c", &cNMEALongitudeCard );

                break;

            case SATELLITES_NUMB:

                sscanf ( psSentenceSlicer, "%d", &iNMEASatellitesNumb );

                break;

            case DILUITION:

                sscanf ( psSentenceSlicer, "%g", &fNMEADiluition );

                break;

            default:

                break;
        }
    }
}
