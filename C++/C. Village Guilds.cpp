#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll NNN = 11;

void pg(vector<vector<ll>>&g){
    for (ll i=0;i<g.size();i++){
        if(g[i].size())
        //cout<<i<<": ";
        for(auto x : g[i])
            cout<<i<<" "<<x<<endl;
        //cout<<endl;
    }
}
void solve(){

    ll n; cin>>n;
    vector<vector<ll>>g(n+1);
    

    for (ll i=2;i<n+1;i++){
        ll fi; cin>>fi;
        g[fi].push_back(i);

    }
    pg(g);



}




int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}