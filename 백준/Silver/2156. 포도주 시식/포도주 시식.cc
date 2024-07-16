#include <iostream>
#include <algorithm>
using namespace std;

int choice[10001];
int dp[2][10001];

int main()
{
	int t;
	cin>>t;
	for(int i=0; i<t; i++)
	{
			cin>>choice[i];
		
	}	
		dp[0][0] = 0;
		dp[1][0] = choice[0];
		dp[0][1] = dp[1][0];
		dp[1][1] = choice[1]+dp[1][0];
		dp[0][2] = choice[0]+choice[1];
		dp[1][2] = max(choice[0]+choice[2],choice[1]+choice[2]);
		dp[0][3] = choice[1]+choice[2];
		dp[1][3] = max(choice[0]+choice[1]+choice[3],choice[0]+choice[2]+choice[3]);
	for(int i=4; i<t; i++)
	{
		dp[0][i]=max(max(dp[0][i-3],dp[1][i-3])+choice[i-1],max(dp[0][i-4],dp[1][i-4])+choice[i-2]+choice[i-1]);
		dp[1][i]=max(max(dp[0][i-2],dp[1][i-2])+choice[i],max(dp[0][i-3],dp[1][i-3])+choice[i-1]+choice[i]);
	}
		
	cout<<max(dp[0][t-1],dp[1][t-1])<<endl;
}
	
	
	
