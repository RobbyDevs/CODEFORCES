#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void print(vector<ll> &v){
    for(auto x:v)cout<<x<<" ";
    cout<<endl;
}

void solve(){
    ll n,k,kk;
    cin>>n>>k;
    kk=k;
    
    vector<ll>v(n);
    vector<ll> vgcd;
    
    for(ll i = 0; i<n; i++)cin>>v[i];

    for(ll i = 0; i<n; i++){
        vgcd.push_back(__gcd(v[i],k));

    }

    print(vgcd);

    for(ll i=0; i<n;i++){
        if (k<=1) break;

        if (vgcd[i]>1){
            k = k/vgcd[i];
            vgcd[i] = 1;
        }
    }

    vector<ll>vans;
    
    for(ll i=0; i<n;i++){
        vans.push_back(abs(vgcd[i]-kk));
        cout<<vgcd[i]<<" - "<<kk<<endl;
    }

    print(vans);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--) solve();
}