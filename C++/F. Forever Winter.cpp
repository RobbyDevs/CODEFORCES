#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n,m;
    ll a,b;
    
    cin>>n>>m;
    vector<vector<ll>> grafo(n);

    for(ll i=0; i<m; i++){
        cin>>a>>b;
        a--;b--;
        grafo[a].push_back(b);
        grafo[b].push_back(a);
    }

    ll uns = 0;
    for(ll i=0;i<n;i++)
        if(grafo[i].size()==1)
            uns++;

    ll x = (n-uns)-1; // 5
    ll y = uns/x;
    cout<<x<<" "<<y<<endl;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
