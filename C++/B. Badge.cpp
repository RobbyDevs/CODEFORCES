#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll>vans;

void dfs(ll p,vector<ll>&g,vector<ll>&vis){

    if(vis[g[p]]){
        vans.push_back(g[p]);
        return;
    }
    
    vis[p]=1;
    //cout<<"indo ao "<<p<<endl;
    dfs(g[p],g,vis);
    
    return;
}
int main(){
    
    ll n; cin>>n;

    vector<ll>g(n+1);
    for(ll i=0;i<n;i++)cin>>g[i+1];
    
    
    for(ll i=1;i<=n;i++){
        vector<ll>vis(n+1,0);
        dfs(i,g,vis);
    }

    for(auto x:vans)cout<<x<<" ";
    cout<<endl;
}