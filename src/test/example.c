
#include <stdio.h>
#include <stdlib.h>


int a, b = 1, c = 2; 
int cnt = 0;
int array[100];


void swap(int a, int b) {
    int temp = array[a];
    array[a] = array[b];
    array[b] = temp;
}

void perm(int start, int end) {
    if (start == end) {
        int i;
        for (i = 0; i <= end; i = i + 1) {
            printf("%d", array[i]);
        }
        printf("\n");
        cnt = cnt + 1;
    } else {

    }
}

void main() {
    
    /* not supported

    for(int i = 0; i < 10; i++);
    for(int i = 0; i < 10; i = i + 1);

    */

    int i = 0;
    for(i = 0; i < 10; i = i + 1);
    
    int j;
    for(i = 0, j = -1; i < 10; i = i + 1, j = j + 1) {
        printf("%d %d\n", i + j, j);

        /* not supported
        
        break;
        continue;
        
        */
    }

    
    scanf("%d", &a);
    
    scanf("%d", array[5]);
    

    return;
}