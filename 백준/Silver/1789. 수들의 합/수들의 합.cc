#include <iostream>

using namespace std;

int main(void){
    long long i = 0;
    long long n = 1;
    cin >> i;
    long long sum = 0;
    int cnt = 0;
    while(true){
        sum = sum + n;
        cnt++;
        if(sum > i){
            cnt--;
            break;
        }
        n++;
    }
    cout << cnt;
    return 0;
}