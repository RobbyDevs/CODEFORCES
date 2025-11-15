#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll l,r;
    cin>>l>>r;

    ll soma = 1;
    ll ans = 0;
    while (l<=r){
        ans++;
        soma = soma+ans;
    }


    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    while(w--)solve();
}