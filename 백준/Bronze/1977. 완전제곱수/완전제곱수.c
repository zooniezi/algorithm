#include <stdio.h>

int main()
{
  int min = 0;
  int max = 0;
  int i = 1;
  int sum = 0;
  int minSquareNum = 0;
  scanf("%d", &min);
  scanf("%d", &max);
  
  
  while(i*i<=max){
    if(i*i<min){
      i++;
      continue;
    }
    else if(minSquareNum == 0){
      minSquareNum = i*i;
      sum += (i*i);
    }
    else{
      sum += (i*i);
    }
    i++;
  }
  
  if(minSquareNum == 0){
    printf("%d", -1);
  }
  
  else{
  printf("%d\n", sum);
  printf("%d", minSquareNum);
  }
  return 0;
}