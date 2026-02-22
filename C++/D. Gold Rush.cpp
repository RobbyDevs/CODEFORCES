#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dfs(ll n, ll k){

    ll a = (n/3) *2;
    ll b = n/3;
    ll ans = 0;
    if (a==k || b == k){
        ans = 1;
        return ans;
    }
    if (a%3==0)
        ans = max(ans,dfs(a,k));
    
    if (b%3==0)
        ans = max(ans,dfs(b,k));
    
    return ans;
}
void solve(){
    ll n,k;
    ll ans = 0;

    cin>>n>>k;
    if (n==k){
        cout<<"YES"<<endl;
        return;
    }

    if (n<k){
        cout<<"NO"<<endl;
        return;
    }
   
    else if(n%3==0)
        ans = dfs(n,k);
    
    if (ans)cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

    
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}