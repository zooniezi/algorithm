#include <iostream>
using namespace std;

int main() {
  int n;
  int checkTwo = 0;
  int checkFive = 0;
  int two = 2;
  int five = 5;

  cin >> n;
  while(1){
    if(n/two==0){
      break;
    }
    checkTwo += n/two;
    two= two*2;
  }
  while(1){
    if(n/five == 0){
      break;
    }
    checkFive += n/five;
    five = five*5;
  }
  cout << checkFive;

}