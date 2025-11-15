#include <bits/stdc++.h>
using namespace std;

int main(){
    int t,i,n;
    cin>>t;

    while (t--) 
    {
        cin>>n;

        vector<int> v(n);
        
        for (i=0;i<n;i++)cin>>v[i];

        int a=0,b=0;
        int aa=a,bb=b;

        for (i=0;i<n;i+=2){
            if (v[i]>a)a=v[i];
            aa++;
        }
        for (i=1;i<n;i+=2){
            if (v[i]>b)b=v[i];
            bb++;
        }
        
        cout<<max(a+aa,b+bb)<<endl;
    }
    
}