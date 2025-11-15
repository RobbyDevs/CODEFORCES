#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    lint t;cin>>t;
    
    for (lint w=0;w<t;w++){
        lint n,k;
        cin>>n>>k;

        if (n%2 == 0) cout<<"YES\n";
        else{
            if (k>n or k%2==0)cout<<"NO\n";
            else cout<<"YES\n";

        }
    }
    return 0;
}