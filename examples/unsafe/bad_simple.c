#include <stdio.h>
#include <string.h>

int main() {
    char src[100] = "hello";
    char dest[10];

    strcpy(dest, src);  // overflow potential
    printf("%s\n", dest);

    return 0;
}
