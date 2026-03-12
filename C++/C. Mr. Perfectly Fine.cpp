#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    ll n;cin>>n;
    ll m1 = 10e6, m10 = 10e6, m11 = 10e6;
    vector<ll>v1,v10,v11;
    
    for(ll i=0;i<n;i++){
        ll a,b; cin>>a>>b;
        if (b==1)v1.push_back(a);
        if (b==10)v10.push_back(a);
        if (b==11)v11.push_back(a);
    }

    if((v1.empty() || v10.empty()) && v11.empty())
        cout<<-1<<endl;
    else{
        for(auto x :v1)m1 = min(m1,x);
        for(auto x :v10)m10 = min(m10,x);
        for(auto x :v11)m11 = min(m11,x);
    
        cout<<min((m1+m10),m11)<<endl;
    }
    

}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll w;cin>>w;
    while(w--)solve();
}
