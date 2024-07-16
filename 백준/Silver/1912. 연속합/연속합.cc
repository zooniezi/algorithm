#include <iostream>
#include <algorithm>
using namespace std;

int dp[100001];
int arr[100001];
int main()
{
	int n;
	cin >> n;
	for(int i=0; i<n; i++) //배열에 값넣기
	{
		cin>>arr[i];
	}
	dp[0]=arr[0];
	int ans=arr[0];
	for(int i=0; i<n; i++)
	{
		
		dp[i+1]=max(dp[i]+arr[i+1],arr[i+1]);
		ans = max(ans, dp[i]);
	}
	cout<<ans;
}
	
	
