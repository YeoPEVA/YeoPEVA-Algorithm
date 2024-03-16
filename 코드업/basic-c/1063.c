#include <stdio.h>

int main(){
    // 3항 연산자 ? 활용.

    /*
    3개의 요소로 이루어지는 3항(ternary) 연산자는
    "조건식 ? (참일 때의 값) : (거짓일 때의 값)” 의 형태로 사용하는 연산자이다.
    - 조건식의 계산 결과가 참인 경우에는 ':' 왼쪽의 값 또는 식으로 바뀌고,
    - 거짓인 경우에는 ':' 오른쪽의 값 또는 식으로 바뀐다.
    */

    int a,b,result;
    scanf("%d %d", &a, &b);

    a>b ? (result = a) : (result = b);

    printf("%d \n", result);
}