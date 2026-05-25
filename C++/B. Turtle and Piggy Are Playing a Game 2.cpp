#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    
    ll n; cin>>n;

    vector<ll>v(n);
    for(ll i=0;i<n;i++)cin>>v[i];
    
    sort(v.begin(),v.end());
    cout<<v[n/2]<<endl;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
