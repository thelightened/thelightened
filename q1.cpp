#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double pi(int i);


int main(){
	int i=0,j;

	printf("Enter j:");
	scanf("%d",&j);
	while(fabs(pi(i+1)-pi(i))>pow(10.0,-j)){
		i++;
	}
	printf("i=%d, Pi_i=%.3lf",i,pi(i));
	system ("pause");
}

double pi(int i){
	double pi_i,pi_tmp;
	pi_tmp = 0;
	for (int j=0;j<=i;j++)
		pi_tmp +=(pow(-1.0,j)*(1.0/(2*j+1)));
	pi_i = 4.0 * pi_tmp;
	return pi_i;
	
}