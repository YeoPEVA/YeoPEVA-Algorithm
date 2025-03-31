#include <stdio.h>

int check_value(int a, int b){
	// printf("input : %d, %d \n", a, b);
	
	if(a > b){
		printf(">");
	}else if(a < b){
		printf("<");
	}else{
		printf("==");
	}
}

int main(int argc, char *argv){
	int input_a, input_b = 0;
	
	scanf("%d %d", &input_a, &input_b);
	
	check_value(input_a, input_b);
	
	return 0;
}



