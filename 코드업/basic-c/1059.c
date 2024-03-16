#include <stdio.h>

int main(){
    int a;
    scanf("%d", &a);
    a = ~a;
    printf("%d \n", a);

    /*
    ** 비트단위(bitwise) 연산자는,
    ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
    <<(bitwise left shift), >>(bitwise right shift)
    가 있다.
    */
}