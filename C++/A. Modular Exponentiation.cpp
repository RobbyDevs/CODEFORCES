#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void solve(){
    ll n,m;
    cin>>n>>m;

    if (n>=27){
        cout<<m<<endl;
    }
    else{
        ll ans = 1;

        for(int i = 1;i<=n;i++)
            ans = ans*2;

        cout<<m%ans<<endl;
    }   
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}