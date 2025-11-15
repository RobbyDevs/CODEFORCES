#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n;
    cin>>n;
    vector<ll>v(n);

    ll ans = 1e17;
    for (ll i = 0; i<n; i++)cin>>v[i];

    for (ll s = 0; s<n; s++){
        ll spell = v[s];
        for(ll i = 0; i<n; i++){

            if (i!=s){ 
                ll x = v[i];
                ll e=v[i],d=v[i];
                if (i<s) d = max(x,((n-1)-i)+v[i]);
                if (i>s) e = max(x,v[i]+i);
                cout<<e<<" "<<d<<" "<<endl;
                x = max(e,d);
                //cout<<x<<endl;
                spell = max(spell,x);
            }
        }
        ans = min(ans,spell);
        
        
    }
    
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}