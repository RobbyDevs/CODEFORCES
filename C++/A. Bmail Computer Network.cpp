#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll>vans;

void dfs(ll p, ll n,map<ll,vector<ll>>&grafo,vector<ll>&vans){
    vans.push_back(p);
    if (p == n){
        for(auto x : vans)cout<<x<<" ";
        cout<<endl;
    }

    for(auto x : grafo[p]){
        dfs(x,n,grafo,vans);
    }
    vans.pop_back();
    return;
}

int main(){

    ll n;cin>>n;

    map<ll,vector<ll>>grafo;

    for(ll i=2; i<n+1; i++){ 
        ll aux; cin>>aux;
        //grafo[i].push_back(aux);
        grafo[aux].push_back(i);

    }

    dfs(1,n,grafo,vans);

    
}