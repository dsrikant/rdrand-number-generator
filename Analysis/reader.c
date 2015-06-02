#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    FILE* in = NULL;
    in = fopen(argv[0], "r");
    uint64_t arr[128];

    // Pass in the position of the one bit here

    // Find how many random numbers there's supposed to be 
    // in a 5G file size
    //fread(arr,sizeof(uint64_t),sizeof(in)/sizeof(uint64_t),in);
    // 80,000,000 64 bit numbers in a 5G file
    fread(arr,sizeof(uint64_t),128,in);

    FILE *f = fopen("res.txt", "w+");
    if (f == NULL){
            printf("Error opening file!\n");
                exit(1);
    }


    // XOR with mask and check == 0
    int mask = 0x0000000000000001;
    for(int i = 0; i < 128; i+=2) {
        if((arr[i]^mask) == 0)
            fprintf(f, "%" PRIx64 "%" PRIx64 "\n", arr[i], arr[i+1]);

    }


    fclose(f);


    /***********************************/
    /***********************************/
    /***********************************/
    /*************This is some scratch work******************/
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
