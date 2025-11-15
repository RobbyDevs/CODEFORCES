#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

void solve(){

    lint n,k,i,j,flag=0;

    cin>>n>>k;

    vector<lint> v;

    if (n%2 == 0){
        if(k>(n/2)){
            cout<<"NO\n";
            flag = 1;
        }
        else{
            for(i=0;i<(k-1);i++){
                v.push_back(2);
            }
            v.push_back((n-(i*2)));
        }
    }
    else{
        if (k%2==0){
            cout<<"NO\n";
            flag = 1;
        }
        else{
            for (i=0;i<(k-1);i++){
                v.push_back(1);
            }
            v.push_back((n-i));
        }

    }

    if (flag==0){
        cout<<"YES\n";
        for (auto j : v) cout<<j<<" ";
        cout<<endl;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    lint t;cin>>t;

    while(t--)
        solve();
}

// 11 4
// 