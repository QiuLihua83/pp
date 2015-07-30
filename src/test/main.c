#include "stdlib.h"
#include "stdio.h"

struct SNode
{
    int n;
    struct  SNode *pNext;

};


int main()
{

    printf("size of SNode is : %lu .\n", sizeof(struct SNode));

    return 0;
}
