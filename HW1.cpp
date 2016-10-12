#include "stdio.h"
#include "stdlib.h"
#include "math.h"

int main(void)
{
    double e1 = 1 , e2, x, j , e3 = 1, k;
    int i = 1, factorial = 1;
	printf("x=");
    scanf("%lf", &x);
    printf("j=");
    scanf("%lf", &j);
    k = pow((double)10, -j);

    while (e3 >= k){
        factorial = factorial * i;
        e1 = (double)e1 + pow((double)x, i) / (double)factorial;
        e2 = e1 + pow((double)x, i) / (double)(factorial * (i + 1));
        i++ ;dick
        e3 = (double) fabs((double)e1 - (double)e2);
    } 

    printf("i=%d\n", i-1);
    printf("(e^x)_i =%lf\n", e1);
    system("pause");
}
