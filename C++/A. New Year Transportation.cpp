#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dfs(ll p, ll n, ll k, vector<ll>&v){
    ll ans = 0;
    //cout<<p<<endl;

    if (p==k)
        return 1;

    if (p+v[p]<=n)
        ans = max(ans,dfs(p+v[p],n,k,v));

    return ans;    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll n,k;
    cin>>n>>k;
    vector<ll>v(n);

    for(ll i=1;i<n;i++)cin>>v[i];

    ll p=1;
    v.push_back(1);
    //cout<<n<<" "<<k<<endl;
    ll ans = dfs(p,n,k,v);

    if (ans)cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

}