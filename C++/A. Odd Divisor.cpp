#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    int t,w,i;
    lint n;

    cin>>t;
    for(w=0;w<t;w++){
        cin>>n;
        double a;
        int b;
        
        if(n%2!=0)cout<<"YES\n";
        else{

            a = log2(n);
            b = a;
            if (a-b == 0)cout<<"NO\n";
            else cout<<"YES\n";
            
        }
    }

}