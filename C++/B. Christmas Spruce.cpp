#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n;
    cin>>n;
    ll aux;


    vector<vector<ll>>grafo(n+1);
    for (ll i = 1; i<n;i++){
        cin>>aux;

        grafo[aux].push_back(i+1);
    }


    for (int i = 1; i<=n; i++){
        cout<<i<<": ";
        for (int j = 0; j<grafo[i].size(); j++){
            cout<<grafo[i][j]<<" ";
        }
        cout<<endl;
    }


}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
}