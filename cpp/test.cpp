#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>

int sum();
bool  chksudoku();
bool chksdk(char ch, char * used);
void resetused(char *used);

int main()
{
    std::cout << "hello, world!" << std::endl;
    sum();
    chksudoku();
}

bool chksudoku()
{
    int arr[9][9] = {{5,3,0,0,7,0,0,0,0},
    		         {6,0,0,1,9,5,0,0,0},
					 {0,9,8,0,0,0,0,6,0},
                     {8,0,0,0,6,0,0,0,3},
                     {4,0,0,8,0,3,0,0,1},
                     {7,0,0,0,2,0,0,0,6},
                     {0,6,0,0,0,0,2,8,0},
                     {0,0,0,4,1,9,0,0,5},
                     {0,0,0,0,8,0,0,7,9}};
    char used[9] = {0};

    for (int i = 0; i < 9; i++)
    {
    	std::cout << "Rows["<< i << "] check begin.........."<<std::endl;
        resetused(used);
        for(int j=0; j<9; j++)
        {
        	if(!chksdk(arr[i][j], used))
        	{
        		std::cout <<"Error row at : " << i << ", " << j <<std::endl;
        		return false;
        	}
        }

        std::cout << "Collums["<< i << "]  check begin.........."<<std::endl;
        resetused(used);
        for(int j=0; j<9; j++)
        {
            if(!chksdk(arr[j][i], used))
            {
            	std::cout <<"Error collum at : " << i << ", " << j <<std::endl;
            	return false;
            }
        }

    }

    std::cout << "Blocks check begin.........."<<std::endl;
    for(int r=0; r<3; r++)
    {
         for(int c=0; c<3; c++)
         {
             resetused(used);
             for(int i=0; i<3; i++)
             {
                 for(int j=0; j<3; j++)
                 {
                     if(!chksdk(arr[r*3+i][c*3+j], used))
                     {
                          return false;
                     }
                  }
              }
         }
    }
    std::cout << "Sudoku is valid!!!.........."<< std::endl;
	return true;
}
bool chksdk(char ch, char * used)
{
	if (0 == ch)
	{
		return true;
	}
	if (used[ch - 1])
	{
		return false;
	}
    used[ch - 1] = true;
    return true;
}
void resetused(char *used)
{
	for (int i=0; i<9; i++)
	{
		used[i] = false;
	}
}

int sum()
{
	int arr[] = {1,2,3,4,5,6,7,8};
	int sum =0;
	for(int i=0; i<sizeof(arr)/sizeof(int); i++)
	{
	    sum += arr[i];
	}
	std::cout << "Sum of arr is : " << sum  << std::endl;
    return sum;
}
