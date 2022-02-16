#include <stdio.h>

char text[15];

int repeats;

void asking ()
{
    printf("Text: ");
    scanf("%s", text);

    printf("Repeats: ");
    scanf("%d", repeats);

    printf("\n\nSENDING %s FOR %d TIMES\n\n", text, repeats);

    asking ();
}

int main ()
{
    asking ();

    return 0;
}
