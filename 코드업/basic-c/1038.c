#include <stdio.h>

int main(){
    // 1073741824 + 1073741824 -> 길이 고려
    long long int a,b;
    
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", a+b);
    
    return 0;
}