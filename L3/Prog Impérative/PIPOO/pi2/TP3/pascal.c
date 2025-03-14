#include "pascal.h"

void pascal(int n) {
    for (int i = 0; i < n+1; i++) {
        for (int j = 0; j < i+1; j++)  
            printf("%ld\t",coefficient(i,j));
        puts("");
    }
}
