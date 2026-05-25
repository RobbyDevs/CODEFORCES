#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    
    ll n; cin>>n;
    string alf = "abcdefghijklmnopqrstuvwxyz";
    vector<ll> freq(26,0);

    priority_queue<
        //  <qtd,ind>
          pair<ll,ll>,vector<pair<ll,ll>>, less<pair<ll,ll>>>fila;

    vector<char>vans;
    for(ll i=0;i<n;i++){
        char aux;cin>>aux;
        freq[aux-97]++;
    }

    pair<ll,ll> ant = {0,0};

    for(ll i=0;i<26;i++)
        if (freq[i]>0) fila.push({freq[i],i});


    for(ll i=0;i<n;i++){
        auto x = fila.top();
        fila.pop();
        
        if (x.first>0){
            x.first--;
            vans.push_back(alf[x.second]);
            
            if (ant.first) fila.push(ant); 
            ant = x;
        }
        if (!fila.size()){
            for(ll j=0;j<x.first;j++)vans.push_back(alf[x.second]);
            break;
        }
    }

    for(auto x:vans) cout<<x;
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
