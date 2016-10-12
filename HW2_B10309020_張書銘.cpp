#include "stdio.h"
#include "stdlib.h"
#include "time.h"

int main(void){
srand(time(NULL));
int true_num[6] ,guess, g_num[6];
int A = 0, C = 5, count = 0;
int i=1, j=0;

do{
	true_num[i] = rand() % 9 + 1 ;
	for (j = 0; j < i ; j++){
		if(true_num[i] == true_num[j]){
			i--;
			break;
		}
	}
	i++;
	}while (i <=5);

while (A != 5){
	A = 0, C = 5;
	printf("Please enter a five digit number.\n");
	scanf("%d", &guess);
	g_num[1] = guess / 10000;	
	g_num[2] = guess % 10000 / 1000;	
	g_num[3] = guess % 1000 / 100;	
	g_num[4] = guess % 100 / 10;	
	g_num[5] = guess % 10;	

	if (guess == 0)
		break;
	else if (guess / 10000 == 0 or guess / 10000 >= 10 )
		printf("This is not a five digit number.\n");
	else	{
		for ( i = 1; i <= 5; i++) {
			for ( j = 1; j <= 5; j++){
				if (g_num[i] == true_num[j] && i == j)
					A++;	C--;	
				else if (g_num[i] == true_num[j])
					C--;
				}
							}
	count++;
	printf("%dA%dC\ncount:%d\n", A, C, count);
	}
	if (A==5)	printf("You win. The correct answer is %d.\n",guess);
	}
	
system("pause");
}