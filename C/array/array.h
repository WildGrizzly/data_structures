#ifndef __ARRAY_H
#define __ARRAY_H

/*



*/

#include <stdint.h>
#define STARTING_LENGTH 32

/* Array */
struct array
  {
     uint64_t length;
     void** data;
     char* type;	
  };

// Initialization.
void array_init(struct array *, char*);
void array_initi(struct array *, uint64_t, char*);

void array_insert();

void array_dealloc(struct array *);

#endif /* array.h */
