#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll sum(vector<ll>vsoma){
    ll soma=0;
    for(auto x:vsoma)soma+=x;
    return soma;
}


void solve(){
    ll n;
    cin>>n;
    vector<ll>v(n);
    vector<ll>freq = {3,1,2,1,0,1,0,0,0,0,0};
    for(ll i=0; i<n; i++)cin>>v[i];

    for(ll i=0; i<n; i++){

        if (freq[v[i]]>0)
            freq[v[i]]-=1;

        if (sum(freq)==0){
            cout<<i+1<<endl;
            return;
        }
    }
    if (sum(freq)>0)cout<<0<<endl;


}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--)solve();
    return 0;
}
