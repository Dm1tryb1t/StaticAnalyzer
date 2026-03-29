#include <stdio.h>
#include <string.h>

int main() {
    char src[100] = "hello";
    char dest[10];

    strncpy(dest, src, sizeof(dest) - 1);
    dest[sizeof(dest) - 1] = '\0';

    printf("%s\n", dest);
    return 0;
}
