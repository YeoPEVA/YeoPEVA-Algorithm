#include <stdio.h>

int main(){
    int a,b,c;
    long long int result; 
    scanf("%d %d %d", &a, &b, &c);
    // double c;
    result = a+b+c;

    // 합, 평균
    printf("%lld \n", result);
    printf("%.1f \n", (double) result / 3);
}