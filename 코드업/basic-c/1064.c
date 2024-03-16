#include <stdio.h>

int main(){
    // 3항 연산자 ? 활용.

    int a,b, c, result;
    scanf("%d %d %d", &a, &b, &c);

    a<b ? (result = a) : (result = b);

    result<c ? (result = result) : (result = c);

    printf("%d \n", result);
}