#include <iostream>
#include <algorithm>
using namespace std;

long long dp[91][2];
long long ans(int n)
{
	dp[1][0]=0;
	dp[1][1]=1;
	dp[2][0]=1;
	dp[2][1]=0;
	for(int i=3; i<=n; i++)
	{
		dp[i][0]=dp[i-1][0]+dp[i-1][1];
		dp[i][1]=dp[i-1][0];
	}
	return dp[n][0]+dp[n][1];
}
int main()
{
	int n;
	cin>>n;
	cout<<ans(n)<<endl;
	
}