
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int iNMEATime           = 0;
int iNMEAControl        = 0;
int iNMEASatellitesNumb = 0;

float fNMEADiluition = 0;

double lfNMEALatitude     = 0;
double lfNMEALongitude    = 0;
double lfNMEAHeightASL    = 0;
double lfNMEAGeoideHeight = 0;

char cNMEAGHUnit;
char cNMEAHASLUnit;
char cNMEALatitudeCard;
char cNMEALongitudeCard;

char sNMEAType[3]      = "";
char sNMEAChecksum[2]  = "";
char sNMEAStationID[4] = "";

char sSentenceGarbage[10] = "";

void NMEA_Parser ()
{
    char sNMEASentence[100];

    strcpy ( sNMEASentence, "$GPGGA,115739.00,4158.8441367,N,09147.4416929,W,4,13,0.9,255.747,M,-32.00,M,01,0000*6E" );

    sscanf ( sNMEASentence, "$GP%[^,],%d.%d,%lg,%c,%lg,%c,%d,%d,%g,%lg,%c,%lg,%c,%d,%[^*]*%s" , sNMEAType, &iNMEATime, sSentenceGarbage, &lfNMEALatitude, &cNMEALatitudeCard, &lfNMEALongitude, &cNMEALongitudeCard, &iNMEAControl, &iNMEASatellitesNumb, &fNMEADiluition, &lfNMEAHeightASL, &cNMEAHASLUnit, &lfNMEAGeoideHeight, &cNMEAGHUnit, sSentenceGarbage, &sNMEAStationID, sNMEAChecksum );

    sSentenceGarbage[0] = 0;

    // printf ( "type:  %s \r\ntime:  %d \r\nlat:  %lg \r\nlatc:  %c  \r\nlong:  %lg \r\nlongc:  %c \r\ncontrol:  %d  \r\nsatnum:  %d  \r\ndil:  %g  \r\nhasl:  %lf %c  \r\ngeoide:  %lf %c  \r\nstat:  %s  \r\ncheck:  %s\r\n", sNMEAType, iNMEATime, lfNMEALatitude, cNMEALatitudeCard, lfNMEALongitude, cNMEALongitudeCard, iNMEAControl, iNMEASatellitesNumb, fNMEADiluition, lfNMEAHeightASL, cNMEAHASLUnit, lfNMEAGeoideHeight, cNMEAGHUnit, sNMEAStationID, sNMEAChecksum );
}
