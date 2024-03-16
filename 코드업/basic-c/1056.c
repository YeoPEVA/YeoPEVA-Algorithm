#include <stdio.h>

int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d \n", (a&&!b)||(!a&&b));
    // 참,거짓이 서로 다른 경우에만 참 출력
}