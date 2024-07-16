#include <iostream>
#include <string.h>
using namespace std;
char arr1[50];
char arr2[50];
char arr3[50];
int main(){
	int num;
	
	cin>>num;
	cin>>arr1;

	for(int i=0; i<num-1; i++)
	{
		cin>>arr2;
		for(int j=0; j<sizeof(arr1)/sizeof(char); j++)
		{
			if(arr1[j]!=arr2[j])
			{
				arr1[j]=63;
			}
		}
	}
	cout<<arr1;
}
	