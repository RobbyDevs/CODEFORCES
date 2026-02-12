#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

bool f(vector<ll>& v,ll val, int tam){
    ll c = 0;

    for(int i = 0; i<tam;i++){
        if(v[i] >= val){
            c++;
            if (c>= val)
                return true;
        }
        else
            c = 0;
    }
    return false;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll n;
    cin>>n;
    vector<ll>v(n);
    
    ll ans = 1;
    ll l = 1;
    ll r = 0;

    for(int i =0; i<n; i++){
        cin>>v[i];
        r = max(r,v[i]);

    }
    
    while (l <= r){
        ll m = (l+r)/2;

        if (f(v,m,v.size())){
            ans = max(m,ans);
            l = m+1;
        }
        else
            r = m-1;
    }
    cout<<ans<<endl;
}