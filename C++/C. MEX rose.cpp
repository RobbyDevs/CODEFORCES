#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n,k, rep = 0;
    cin>>n>>k;

    vector<ll>v(n);
    set<ll> z;
    

    for (ll i = 0; i<n; i++){
        ll val; cin>> val;
        
        if (val < k) z.insert(val);
        if (val == k) rep++;

    }

    ll valoresAteK = k-z.size();

    ll ans = max(valoresAteK,rep);
    cout<<ans<<endl;

    //for (ll x : v) cout<<x<<" ";
    //cout<<"\n";

}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin >>w;
    while(w--){
        solve();
    }
}

/*

verificar quantos numeros  em v sao menores que k (z);

para mex(x) == k, vao ser necessarias z operacoes

se k aparece mais que z vezes (x vezes), entao o resultado eh x.

*/