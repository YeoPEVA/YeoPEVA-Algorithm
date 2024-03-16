#include <stdio.h>

int main(){
    int a,b;

    scanf("%d.%d",&a,&b);

    printf("%d \n",a);
    printf("%d \n",b);

    /*
    !!
    scanf("%lf", &a);
    
    printf("%.lf \n",a);
    printf("%lf \n", a - (int)a);
    */

    return 0;
}