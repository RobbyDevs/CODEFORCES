#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> div(ll n){

    vector<ll>v;
    ll i =1;

    while (i*i <= n){
        if (n%i ==0){
            v.push_back(i);

            if (i != n/i)
                v.push_back(n/i);
        }
        i++;
    }

    
    return v;
}
void solve(){
    ll n; cin>>n;
    ll ans = 0;

    for(ll i = 1;i<=n;i++){
        vector<ll>v=div(i);
        //cout<<i<<" >>>>"<<v.size()<<endl;

        for (auto x:v)
            //if (x>1)
            ans+= (n/x);
    }

    cout<<ans<<endl;

    

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while (w--)
        solve();
    
    
}