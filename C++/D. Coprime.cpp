#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n;
    cin>>n;
    map<ll,ll>dic;

    for(ll i=0;i<n;i++){
        ll x; cin>>x;
        dic[x]=i+1;
    }

    ll ans = 0;

    for(auto x : dic){
        for(auto y : dic){
            if (__gcd(x.first,y.first)==1){
                ans = max(ans,x.second+y.second);
            }
        }
    }
    
    if(!ans) cout<<-1<<endl;
    else cout<<ans<<endl;




}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;

    while(w--){
        solve();
    }
}
