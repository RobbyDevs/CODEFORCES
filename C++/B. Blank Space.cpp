#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n; cin>>n;
    ll c =0;
    ll ans = 0;

    for(ll i=0;i<n;i++){
        ll a;cin>>a;
        if (a==0)c++;
        else{
            ans=max(ans,c);
            c = 0;
        }
    }

    cout<<max(ans,c)<<endl;
    
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
