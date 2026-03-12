#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAXN 20

vector<ll> dp(MAXN,0);
vector<vector<ll>>grafo(MAXN);

void pg(vector<vector<ll>>&grafo){

    for(ll i=0;i<grafo.size();i++){
        cout<<i<<": ";
        for (ll j = 0;j<grafo[i].size();j++){
            cout<<grafo[i][j]<<" ";
        }
        cout<<endl;
    }
    
}

void build(vector<vector<ll>>& grafo){
    ll nivel = 1;
    ll p =0;
    
    for(ll i=1; i<=9;i++){
        p++;
        //e
        grafo[i].push_back(i+nivel);
        grafo[i+nivel].push_back(i); 
        //d
        grafo[i].push_back(i+nivel+1);
        grafo[i+nivel+1].push_back(i);
        
        
        if (p>=nivel){
            nivel++;
            p=0;
        }
    }
    //pg(grafo);
}

long long dfs(ll p, vector<vector<ll>>& grafo, vector<ll> &vis){
    cout<<"p>> "<<p<<endl;
    if (dp[p] != 0 && !vis[p]){
        cout<<p<<" ja na pd: "<<dp[p]<<endl;
        return dp[p];
    }
    ll pdx = 0;
    
    if (!vis[p]){
        cout<<"visitando "<<p<<endl;
        ans = p*p;
        vis[p] =1;
        for (auto x : grafo[p]){
            if (x < p){
    
                //cout<<p<<" -> "<<x<<endl;
                //cout<<ans<<endl;
                ans+= dfs(x,grafo,vis);
            }
        }

    }
    cout<<"ans >> "<<ans<<endl;
    return dp[p] = ans;

}



void solve(){
    ll n;cin>>n;

    vector<ll>vis(MAXN+1);
    ll ans;
    //pg(grafo);

    ans = dfs(n,grafo,vis);
    cout<<">>>"<<ans<<endl;


}
int main(){
    //ios::sync_with_stdio(0);
    //cin.tie(0);
    build(grafo);
    //cout<<"build OK"<<endl;
    ll w;cin>>w;
    while(w--){
        solve();
        cout<<"DP: ";
        for(auto x:dp)cout<<x<<" ";
        cout<<endl;

    }
    
}

/*

verE = i+nivel
verD = i+nivel+1

*/


