// 函数调用测例
// 函数参数不能是数组, 只能是普通变量

#include<stdio.h>
#include<string.h>

int cnt[10];

void init(int n, int value) {
    int i;
    for(i = 0; i < n; i = i + 1) {
        cnt[i] = value;
        value = value + 1;
    }
    return;
}
void print(int n) {
    int i;
    for(i = 0; i < n; i = i + 1) {
        printf("%d ", cnt[i]);
    }
    printf("\n");
    return;
}

int main()
{

    int n = 10;
    int value = 2;
    init(n, value);
    print(n);
    return 0;
}