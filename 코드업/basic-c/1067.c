#include <stdio.h>

int main(){
    int a;
    scanf("%d", &a);

    if(a%2 == 0){
        if(a > 0){
            printf("plus \n");
        }
        printf("even \n");
        
    }else{
        if(a > 0){
            printf("plus \n");
        }
        printf("odd \n");
    }
}