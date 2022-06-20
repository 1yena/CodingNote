#include <stdio.h>

int q(int a, int b) {
    int c = a + b;
    return c;
}

int main() {
    int k;
    k = q(5, 7);

    printf("%d", k);

    return 0;
}