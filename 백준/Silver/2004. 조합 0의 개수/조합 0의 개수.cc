#include <iostream>
using namespace std;
int countFive(long long int num){
		int fivecnt=0;
		for(long long int i = 5; (num/i)>=1; i=i*5){
			fivecnt += (num/i);
		}
		return fivecnt;
	}
	int countTwo(long long int num){
		int twocnt=0;
		for(long long int i = 2; (num/i)>=1; i=i*2){
			twocnt += (num/i);
		}
		return twocnt;
	}
int main(){
	long long int n,m;
	cin >> n >> m;
	
	int numOfFive = countFive(n);
	if(m != 0){
		numOfFive -= countFive(m);
	}
	if(m != n){
		numOfFive -= countFive(n-m);
	}
	int numOfTwo = countTwo(n);
	if(m != 0){
		numOfTwo -= countTwo(m);
	}
	if(m != n){
		numOfTwo -= countTwo(n-m);
	}
	if(numOfTwo>numOfFive){
		cout << numOfFive;
	}
	if(numOfTwo<=numOfFive){
		cout << numOfTwo;
	}
}
