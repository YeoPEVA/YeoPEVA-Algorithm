#include <stdio.h>

int main(){
    int a;
    scanf("%d", &a);
    printf("%d \n", !a);

    /*
    printf("%d", !0); //거짓의 반대, 즉 참인 1로 계산됨
    printf("%d", !1); //참의 반대, 즉 거짓인 0으로 계산됨
    printf("%d", !999); //참의 반대, 즉 거짓인 0으로 계산됨
    참, 거짓의 논리값(boolean value)인 불 값을 다루어주는 논리연산자는
    !(not), &&(and), ||(or) 이 있다.
    */
}