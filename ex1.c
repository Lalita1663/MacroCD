/*
Lalita Purohit
Nidhi Jangir

SIngle line Macro  ( More then one Macro can be defined )

*/

#include<stdio.h>
$def AND && @end
$def OR  || @end

int main()
{
        int f=1,x=4,y=90;
        
        if((f<5) AND (x<=20 OR y<=45))
        
                printf("Your PC will always work fine...\n");
        else
                printf("Infront of the maintenance man\n");        
        return 0;


}



