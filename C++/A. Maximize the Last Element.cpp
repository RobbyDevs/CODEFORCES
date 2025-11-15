#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n;
        cin >> n;
        vector<ll>v(n);

        for (ll i = 0; i<n; i++)cin>>v[i];
        ll ans = 0;
        for (ll i = 0; i<n;i++){
            if( i %2 ==0){
                ans = max(ans,v[i]);
            }
        }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin>>t;
    while(t--) solve();

}