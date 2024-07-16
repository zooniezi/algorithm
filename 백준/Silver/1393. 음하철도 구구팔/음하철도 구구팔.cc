#include <iostream>
#include <math.h>
using namespace std;
int main(){
	float stationX, stationY, nowX, nowY, moveX, moveY, semiX, semiY = 0;
	cin >> stationX >> stationY >> nowX >> nowY >> moveX >> moveY;
	float dt = (((stationX*moveX)+(stationY*moveY))-((nowX*moveX)+(nowY*moveY)))/((moveX*moveX) + (moveY*moveY));
	if(dt<=0){
		cout<< nowX << " " << nowY;
	}
	else{
		cout<< nowX + moveX*dt << " " << nowY + moveY*dt;
	}
}
