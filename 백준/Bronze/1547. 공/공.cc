#include <iostream>
using namespace std;
 
int location[4]={0,1,2,3};
 
void swap(int x, int y){
    int temp=location[x];
    location[x]=location[y];
    location[y]=temp;
    return;
}
int main(){
    
    int M;
    cin>>M;
    
    for(int i=0;i<M;i++){
        int x,y;
        scanf("%d %d",&x,&y);
        swap(x,y);
    }
    
    for(int i=1;i<=3;i++){
        if(location[i]==1)
            cout<<i<<endl;
    }
    return 0;
}
 