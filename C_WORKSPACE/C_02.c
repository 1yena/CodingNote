#include <stdio.h>

void q(int a, int b) {
    int c = a + b;

    printf("%d", c);
    return;
}

int main() {
    q(7, 10);
    return 0;
}