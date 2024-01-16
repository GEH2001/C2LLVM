#include <stdio.h>	
#include <stdlib.h>
#include <string.h>

int main()
{
    int array[100];
    char str[200];
    printf ("Please type the numbers (separated by a comma):\n");
    scanf ("%s", &str);
	int p, q, r, n, len;
	p = q = r = n = 0;
	len = strlen(str);
	char buf[20];
    while (p < len) {
		if (str[p] == ',') {
			r = 0;
			while (q < p) {
				buf[r] = str[q];
				r = r + 1;
				q = q + 1;
			}
			array[n] = atoi (buf);
			n = n + 1;
			p = p + 1;
			q = p;
			for (r = 0; r < 20; r++)
				buf[r] = '\0';
		}
		else if (p == len - 1) {
			r = 0;
			while (q <= p) {
				buf[r] = str[q];
				r = r + 1;
			}
			array[n] = atoi (buf);
			n = n + 1;
			p = p + 1;
			for (r = 0; r < 20; r++)
				buf[r] = '\0';
		}
		else {
			p = p + 1;
		}
	}
	int i, j, temp;
	for (i = 1; i < n; i = i + 1)
	{
		for (j = 0; j < n - i; j = j + 1)
		{
			if (array[j] > array[j + 1])
			{
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}
	for (i = 0; i < n; i = i + 1) {
        printf("%d", array[i]);
        if (i < n -1){
            printf (",");
		}
    }
    return 0;
}