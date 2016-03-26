#include <math.h>

/*
gcc -Wall -Wextra -O -ansi -pedantic -shared euler_c.c -o euler_c.so

*/

long square_sum_of_digits(long x){
    int s=0;
    while(x)
    {
        s += pow(x%10,2);
        x /= 10;
    }
    return s;
}
