#include <stdio.h>
#include <string.h>

int main() {
    char a[10], b[100] = "test";

    strcpy ( a , b ); // overflow potential
    sprintf (a, "%s", b);

    return 0;
}
