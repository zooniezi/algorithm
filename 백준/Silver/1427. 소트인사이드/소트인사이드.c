#include <stdio.h>

int main(){
  int num = 0;
  int i,j;
  int temp = 0;
  int len = 0;
  int arr[11] = {0,};
  scanf("%d", &num);

  for(i = 0; i<11; i++){
    arr[i] = num%10;
    num = num/10;
    if(num != 0){
      len++;
    }
  }


  for(j=0; j<10; j++){
      for(i=0; i<10-j; i++){
        if(arr[i]<arr[i+1]){
          int temp = arr[i+1];
          arr[i+1] = arr[i];
          arr[i] = temp;
        }
      }
  }

  for(i=0; i<len+1; i++){
    printf("%d", arr[i]);
  }

}