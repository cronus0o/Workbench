#include <stdio.h>
#include <stdlib.h>

int main() {
    char command[1024];

    while (1) {
        printf("> ");
        fgets(command, sizeof(command), stdin);
        system(command);
    }

    return 0;
}


