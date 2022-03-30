#include <stdio.h>
int print(a){
    printf("%d\n",a);
}
// 메모리를 어떻게 하면 더 줄일 수 있을까? 내일 찾아보기.
int main(void){
    int A, B;
    scanf("%d %d", &A, &B);
    print(A+B);
    print(A-B);
    print(A*B);
    print(A/B);
    print(A%B);
    return 0;
}