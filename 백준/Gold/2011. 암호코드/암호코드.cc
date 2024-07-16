#include <iostream>
#include <string>
using namespace std;

long long dp[5001];
int arr[5001];
long long finalanswer[5001];
int main()
{
	arr[0]=0;
	dp[0]=1;
	string ans;
	cin>>ans;
	int s=ans.length();
	for(int i=1; i<=s; i++)
	{
		arr[i]=ans[i-1]-'0';
	}
	//cout<<arr[1]<<endl;
	//cout<<arr[2]<<endl;
	for(int j=1; j<=s; j++)
	{
		if(arr[j]>0)
		{
			dp[j]=dp[j]+dp[j-1];
			dp[j]=dp[j]%1000000;
		}
		if(arr[j-1]*10+arr[j]>=10 && arr[j-1]*10+arr[j]<=26)
		{
			dp[j]=dp[j]+dp[j-2];
			dp[j]=dp[j]%1000000;
		}
	
	}
	cout<<dp[s];
}
	
	
