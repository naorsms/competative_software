#include <stdio.h>

int main() {
    long  Q;
    long  a, b;
    long  sum ;
    scanf("%ld", &Q);
    long i ;
    for(i=0;i<Q;i++){
        sum = 0;
        scanf("%ld %ld", &a, &b);
        while(a != b){
            if(a>b){
                sum++;
                a = a/2;
            }
            if(b>a){
                sum++;
                b = b/2;
            }
        }
         printf("%ld", sum);
         printf("\n");
    }
    
   
    return 0;
}