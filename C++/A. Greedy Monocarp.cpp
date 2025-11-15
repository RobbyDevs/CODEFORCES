#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void solve(){

    ll n,k;
    cin>>n>>k;

    vector<ll>v(n);

    ll soma = 0;
    for (ll i = 0; i<n; i++){
        cin>>v[i];
        soma+=v[i];
    }
    if (soma<=k) cout<<k-soma<<endl;
    else{
        soma = 0;
        sort(v.rbegin(),v.rend());

        for (ll i = 0; i<n;i++){
            if (soma + v[i] > k)
            {
                cout<<k-soma<<endl;
                break;
            }
            soma+=v[i];
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int w; cin>>w;
    while(w--)solve();
}