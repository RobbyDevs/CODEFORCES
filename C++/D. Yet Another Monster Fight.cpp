#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n;
    cin>>n;
    vector<ll>v(n);
    vector<ll>e(n);
    vector<ll>d(n);
    ll ans = 1e17;

    for (ll i = 0; i<n; i++)cin>>v[i];

    for (int i = 0; i<n;i++){
        e[i] = ((n-1)-i)+v[i];
    }
    
    for (int i = 0; i<n; i++){
        d[i] = v[i]+i;
        
    }

    for (int i = 1; i < n; i++) {
        e[i] = max(e[i], e[i-1]);
    }

    for (int i = n-2; i >= 0; i--) {
        d[i] = max(d[i], d[i + 1]);
    }

    //for (int i = 0; i<n;i++){
        //cout<<e[i]<<" "<<d[i]<<endl;
    

    for (int i = 0; i<n;i++){
        ll x = v[i];

        if (i>0) x = max(e[i-1],x);
        if (i+1<n) x = max(d[i+1],x);

        ans = min(ans,x);
    }
    cout<<ans<<endl;

    
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}