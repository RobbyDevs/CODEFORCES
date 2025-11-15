#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void print(vector<ll> &v){
    for(auto x:v)cout<<x<<" ";
    cout<<endl;
}


void solve(){
    ll n,k;
    cin>>n>>k;
    vector<ll>v(n);
    
    for(ll i=0; i<n; i++)cin>>v[i];

    sort(v.begin(),v.end());

    ll l =0, r = n-1;

    print(v);
    
    ll ans = 0;

    while(k--){
        if(v[l]+v[l+1] > v[r]){
            r--;
        }
        else{
            l+=2;
        }
    }

    for(ll i = l; i<=r;i++){
        ans+=v[i];
    }
    cout<<ans<<endl;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;

    while(w--){
        solve();
    }
}

/*
15 22 12 10 13 11
10 11 12 13 15 22

10 21 33 36 51 73

*/