#include <bits/stdc++.h>
using namespace std;
typedef long lint;
int main(){
    lint c,n,t;

    cin>>t;
    for (lint w=0;w<t;w++){


        cin>>n;
        vector<lint> v(n);
        for (lint i=0;i<n;i++)cin>>v[i];

        //sort(v.begin(),v.end());

        for (lint i:v) cout<<(n+1)-i<<" ";
        cout<<endl;
        
    }
    return 0;
    
}
