#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int a;
	int n;
	bool checker = false;
	cin >> a;
	if(a<8){
		cout << -1;
		return 0;
	}
	if(a%2==0){
		cout << "2 2 ";
		n= a-4;
	}
	else{
		cout << "2 3 ";
		n = a-5;
	}
	for(int i = 2; i<n; i++){
		for(int j=2; j<i; j++){
			if(i%j==0){
				checker = true;
				break;
			}
		}
		for(int k=2; k<n-i; k++){
			if((n-i)%k==0){
				checker = true;
				break;
			}
		}
		if(!checker){
			cout << i << " " << n-i;
			break;
		}
		checker = false;
	}
}
