#include <stdio.h>

int main(){
    int i = 0;

    char d[30];

    scanf("%s", d);

    for(i=0;d[i]!='\0';i++)
    {
        printf("\'%c\' \n", d[i]);
    }
    // \0, NULL -> 널문자 체크 
    return 0;
}