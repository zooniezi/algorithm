#include <iostream>
#include <string>
using namespace std;

int date[13];
int main()
{
	date[1]=31;
	date[2]=28;
	date[3]=31;
	date[4]=30;
	date[5]=31;
	date[6]=30;
	date[7]=31;
	date[8]=31;
	date[9]=30;
	date[10]=31;
	date[11]=30;
	date[12]=31;
	int x,y,total;
	cin>>x>>y;
	total = 0;
	for(int i =1; i<x; i++)
	{
		total= total+date[i];
	}
	total = total+y;
	int day = total%7;
	if(day==1)
	{
		cout<<"MON";
	}
	else if(day==2)
	{
		cout<<"TUE";
	}
	else if(day==3)
	{
		cout<<"WED";
	}
	else if(day==4)
	{
		cout<<"THU";
	}
	else if(day==5)
	{
		cout<<"FRI";
	}
	else if(day==6)
	{
		cout<<"SAT";
	}
	else if(day==0)
	{
		cout<<"SUN";
	}
	
}
	
