#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    int n; cin>>n;
    vector<ll> v(n);

    for(int i = 0; i<n; i++) cin>>v[i];

    for (int i =0; i<n-1; i++){
        if (v[i] == 1) v[i]++;
        if (v[i+1]%v[i] == 0)
            v[i+1]++;
    }
    for( ll x:v) cout<<x<<" ";
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;

    while(w--){
        solve();
    }
}


/*

*/