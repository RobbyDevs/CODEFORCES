#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void print(vector<ll> &v){
    for(auto x:v)cout<<x<<" ";
    cout<<endl;
}

void solve(){
    ll n,k;
    cin>>n>>k;
    vector<ll>v(n);
    vector<ll>vans;
    ll m=0;

    for(ll i=0; i<n; i++){
        ll x; cin>>x;
        x = x%k;
        
        if(!x)v[i]=k;
        else v[i]=x;
    }
    priority_queue<pair<ll,ll>> fila;

    for(ll i=0; i<n; i++){
        fila.push({v[i],-i});
    }

    for(ll i = 0; i<n;i++){
        pair<int,int>pont = fila.top();
        fila.pop();
        pont.first-=k;
        if (pont.first<=0)
            vans.push_back((pont.second-1)*-1);
        fila.push(pont);
    }

    print(vans);

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--){
        //cout<<">>>>>>>>";
        solve();
    }
}

/*
3
2835
8532


*/