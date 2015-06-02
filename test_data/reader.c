#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv) {
    FILE* in = NULL;
    in = fopen(argv[0], "r");
    uint64_t arr[128];

    // Find how many random numbers there's supposed to be 
    // in a 5G file size
    //fread(arr,sizeof(uint64_t),sizeof(in)/sizeof(uint64_t),in);
    fread(arr,sizeof(uint64_t),128,in);

    for(int i = 0; i < 128; i++) {
        printf("%" PRIx64 "\n", arr[i]);
    }

    //for (int i = 0; i < sizeof(in)/sizeof(uint64_t); i++){
    // Print out a couple numbers at first so we make sure it's running properly.
    /*for (int i = 0; i < 5; i++){
        // Do the math on each number here
        // Stick results in a new array
        // Write all the results to a new file
      //  printf("%d\n", arr[i]);
    } */

    fclose(in);
}

/* Python Code */

// 1. Call the C module to read new data from all files
// 2. Read data from the output file into a dict, and quicksort it
// 3. Write the sorted array back to file
// 4. Send the sorted array to dcswitch90 "scratch"
// 5. On 90 split up the work of merging amongst four servers
// 6. Parse the totally sorted list and record duplicates.
