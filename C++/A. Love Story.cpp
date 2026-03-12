#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    string s; cin>>s;
    string vs = "codeforces";
    
    ll ans= 0;
    for(ll i=0;i<s.size();i++)
        if (s[i]!=vs[i])ans++;
        
    cout<<ans<<endl;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
