#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;cin>>t;

    for (int w=0; w<t;w++){
        int n; cin>>n;

        string v;
        cin>>v;
        string s = "Timur";
        sort(s.begin(),s.end());

        sort(v.begin(),v.end());
        
        
        if (v== s) cout<<"YES\n";
        else cout<<"NO\n";
    }
}