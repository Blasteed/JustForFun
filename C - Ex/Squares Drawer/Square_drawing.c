#include <stdio.h>

// var having square's dimensions
int s;

// var having a code reboot counter
int reboots = 1;

// func using scanf, without the code looks slower
int asking ()
{
    // \n formatting
    printf("\n");

    printf("Dimensions? ");
    scanf("%d", &s);

    // if the selected dimensions are under 2 it will give an error and repeat the func
    if (s < 2)
    {
        printf("\n\nERRORE! - SELEZIONARE UN VALORE MAGGIORE O UGUALE A 2\n\n");

        asking ();
    }

    else
    {
        drawing ();
    }

    return 0;
}

int drawing ()
{
    // \n formatting
    printf("\n");

    // the for printing the height
    for (int i = 1; i <= s; i++)
    {
        // printing with spaces formatting
        printf("    * ");

        // if is printing in starting or ending row it will echo asterisks
        if (i == 1 || i == s)
        {
            // the for printing the length, the "-2" is used to subtract the "only filling asterisks" to create the right dimensioned square
            for (int j = 1; j <= s - 2; j++)
            {
                printf("* ");
            }

            // ending asterisk
            printf("*");
        }

        // else it will echo spaces
        else
        {
            for (int j = 1; j <= s - 2; j++)
            {
                printf("  ");
            }

            // ending asterisk
            printf("*");
        }

        // \n formatting
        printf("\n");
    }

    // the var calculating the area
    int area = s * s;

    // printing area
    printf("\nSquare area:  %d ^ 2 = ", s);
    printf("%d", area);

    // \n formatting
    printf("\n");

    // reboot printing, recalling "main ()", with funny reboot calculating
    printf("\n\nREBOOT!\nSQUARES GENERATED: %d\n\n", reboots);

    reboots++;

    main ();

    return 0;
}

int main ()
{
    // calling the starting func
    asking ();

    return 0;
}
