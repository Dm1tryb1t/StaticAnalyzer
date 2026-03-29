#include <stdio.h>

int main() {
    char buffer[50];

    gets(buffer);  // dangerous
    sprintf(buffer, "User input: %s", buffer);  // dangerous

    system("ls");  // dangerous

    return 0;
}
