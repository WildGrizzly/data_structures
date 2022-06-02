#include "array.h"
#include <stdlib.h>
#include <stdint.h>

void array_init(struct array* new_array, char* type) {
    new_array->data = malloc(STARTING_LENGTH * sizeof(void*));   
    new_array->length = STARTING_LENGTH;
    new_array->type = type;
}

void array_initi(struct array* new_array, uint64_t len, char* type) {
    new_array->data = malloc(len * sizeof(void*));
    new_array->length = len;
    new_array->type = type;
}

void array_dealloc(struct array* dispose_array) {
    free(dispose_array->data);
}
