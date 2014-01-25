#include "stdlib.h"

int main(int argc, char** argv){

    if(argc < 2) return 1;

    printf("%s%s",argv[1], argv[2]);

    return 0;
}
