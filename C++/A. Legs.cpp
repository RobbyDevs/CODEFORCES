#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n; cin>>n;
    ll ans = n/4;
    ll mod = n%4;
    if (mod==0)cout<<ans<<endl;
    else cout<<ans+1<<endl;
}
int main(){
    ll w;cin>>w;
    while(w--)solve();
}