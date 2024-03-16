#include <stdio.h>

int main(){
    int a,b,c,d,e = 0;

    scanf("%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e);
    
    printf("[%d0000]\n", a);
    printf("[%d000]\n", b);
    printf("[%d00]\n", c);
    printf("[%d0]\n", d);
    printf("[%d]\n", e);
    
    return 0;
}