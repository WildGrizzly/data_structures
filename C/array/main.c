#include "array.h"
#include <stdlib.h>
#include <stdio.h>

int main() {
   struct array test;
   array_init(&test, "int");
   
   array_dealloc(&test);
}
