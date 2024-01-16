#include<stdio.h>
#include<string.h>

int main()
{
    int i,j;
    char s[80];
    printf("Please type a string:\n");
    scanf("%s", &s);
    int flag = 1;
    for(i=0,j=strlen(s)-1;i<j;i=i+1,j=j-1)
    {
        if(s[i]!=s[j]){
            flag = 0;
        }
    }
    if(flag){
        printf("True\n",s);
    }
    else{
        printf("False\n",s);
    }
    return 0;
}
