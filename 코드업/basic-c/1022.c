#include <stdio.h>

int main(){
    char data[2001];
    fgets(data, 2000, stdin);
    // scanf, fgets 
    printf("%s", data);

    return 0;
}