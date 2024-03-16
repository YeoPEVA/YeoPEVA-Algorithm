#include <stdio.h>

int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    // double c;

    // 합, 차, 곱, 몫, 나머지, 나눈 값 
    printf("%d \n", a+b);
    printf("%d \n", a-b);
    printf("%d \n", a*b);
    printf("%d \n", a/b);
    printf("%d \n", a%b);
    // printf("%f \n", c);
    printf("%.2f\n", (double) a / (double) b); // 출력 결과 33.333333
}