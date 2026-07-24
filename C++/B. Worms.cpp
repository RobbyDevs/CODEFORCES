#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void pv(vector<ll>v){
    for (auto x:v)cout<<x<<" ";
    cout<<endl;
}

ll bs(ll e, ll d, ll x, vector<ll>&v){
    ll m = (e+d)/2;
    if (e>=d || v[m]==x)
        return m;

    if(v[m]>x)
        d = m;

    if(v[m]<x)
        e = m+1;
    

    return 0+ bs(e,d,x,v);

}
void solve(){
    ll n;cin>>n;
    vector<ll>v(n);
    vector<ll>vp;
    for(ll i=0;i<n;i++){
        cin>>v[i];
        if(vp.empty()) vp.push_back(v[i]);
        else vp.push_back(vp[i-1]+v[i]);
    }

    //pv(vp);

    ll m; cin>>m;
    for(ll i = 0;i<m;i++){
        ll x; cin>>x;
        cout<<bs(0,n,x,vp)+1<<endl;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}


