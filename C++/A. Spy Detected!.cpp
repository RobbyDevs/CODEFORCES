#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){

    vector<pair<ll,ll>> v(110);

    ll n;
    cin>>n;
    
    for(ll i=0;i<n;i++){
        ll aux;
        cin>>aux;
        v[aux].first++;
        v[aux].second = i;
    }
    
    for(ll i=0;i<110;i++){
        if(v[i].first==1){
            cout<<v[i].second+1<<endl;
            return;

        }
    }
    

}

int main(){
    ll w;cin>>w;
    while(w--)solve();
}