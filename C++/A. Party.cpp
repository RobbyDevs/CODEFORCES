#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dfs(ll p,vector<ll>& grafo) {
    if (grafo[p] == -1)
        return 1;
    
    return 1 + dfs(grafo[p],grafo);
}

int main() {
    ll n;
    cin>>n;
    vector<ll>grafo(n+5);

    for (ll i=1; i<=n; i++) {
        cin >> grafo[i];
    }

    ll ans=0 ;
    for (ll i=1; i<=n; i++)
        ans = max(ans,dfs(i,grafo));

    cout<<ans<<endl ;


}