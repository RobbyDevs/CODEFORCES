#include <bits/stdc++.h>
using namespace std;

int main(){

    int t; cin>>t;
f
    for (int w=0; w<t;w++){
        int n,a,b;
        cin>>n>>a>>b;

        if(a == b && a == n)cout<<"YES\n";
        else{
            if (a + b >= n-1)cout<<"NO\n";
            else cout<<"YES\n";
        }
    }
}




