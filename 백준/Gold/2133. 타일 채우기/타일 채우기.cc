#include <iostream>
#include <algorithm>
using namespace std;

long long dp[31];
int main()
{
	int n;
	cin>>n;
	dp[0]=1;
	dp[2]=3;
	for(int i=4; i<=n; i=i+2)
	{
		dp[i]=dp[i]+dp[i-2]*3;	
		for(int j=i-4; j>=0; j=j-2)
		{
			dp[i]=dp[i]+2*dp[j];
		}
	}
	cout<<dp[n];
}
	
	
