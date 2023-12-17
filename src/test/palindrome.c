#include<stdio.h>
#include<string.h>

int main()
{
    int i,j;
    char s[80];
    printf("Please type a string:\n");
    scanf("%s", &s);
    for(i=0,j=strlen(s)-1;i<j;i++,j--)
    {
        if(s[i]!=s[j])
            break;
    }
    if(i<j)
        printf("False\n",s);
    else
        printf("True\n",s);
    return 0;
}
