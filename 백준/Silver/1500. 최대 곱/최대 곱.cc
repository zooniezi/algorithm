#include <iostream>
using namespace std;
long long int array[20] = {0,};
int main(){
	int s;
	int k;
	cin >> s >> k;

	for(int i = 0; i<k; i++){
		array[i]+=(s/k);
	}
	for(int i =0; i<(s%k); i++){
		array[i]++;
	}
	long long int ans = 1;
	for(int i=0; i<k; i++){
		ans = ans * array[i];
	}
	cout << ans;
}
