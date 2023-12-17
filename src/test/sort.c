#include <stdio.h>	
#include <stdlib.h>
#include <string.h>

int main()
{
    int array[100];
    char str[200];
    printf ("Please type the numbers (separated by a comma):\n");
    scanf ("%s", &str);
    char seps[] = ",";
	char* s1 = NULL;
    int n = 0;
	for (s1 = strtok(str,seps); s1 != NULL; s1 = strtok(NULL,seps))
	{
		array[n++] = atoi(s1);
	}

	// calculate
	int i, j, temp;
	for (i = 1; i < n; i++)
	{
		for (j = 0; j < n - i; j++)
		{
			if (array[j] > array[j + 1])
			{
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
	for (i = 0; i < n; i++) {
        printf("%d", array[i]);
        if (i < n -1)
            printf (",");
    }
    return 0;
}