#include <stdio.h>
#include <stdlib.h>
#include<time.h>

int fibonacci(int n),fibonacci_recursion(int n);

int main(){
        int n,ans;
		long start,end;
        printf("Enter an integer:");
        scanf("%d", &n);
		
		//非遞迴版時間
        start = clock();
        for (long i = 1; i <= 1000000; i++)
                ans = fibonacci(n);
        end = clock();
        printf("Nonrecursion total time = %1.3f seconds\n", (end - start) / 1000.0 );
		
		
		//遞迴版時間
		start = clock();
        for (long i = 1; i <= 1000000; i++)
                ans = fibonacci_recursion(n);
        end = clock();
		printf("Recursion total time = %1.3f seconds\n", (end - start) / 1000.0);
		
		
		
        printf("Ans:%d\n", ans);
        system("pause");

}

//非遞迴版
int fibonacci(int n){
        int tmp0 = 0, tmp1 = 2,ans;
        if (n == 0)
                ans = tmp0;
        else if (n == 1)
        ans = tmp1;
        else
        {
                for (int i = 2; i <= n; i++){
                        ans = tmp1 + 2 * tmp0;
                        tmp0 = tmp1;
                        tmp1 = ans;
                }
        }
        return ans;
}

//遞迴版
int fibonacci_recursion(int n){

	    if (n == 0)
            return 0;
        else if (n == 1)
			return 2;
        else
        	return fibonacci_recursion(n - 1) + 2 * fibonacci_recursion(n - 2); 
}