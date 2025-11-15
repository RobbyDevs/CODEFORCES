#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n;
    cin>>n;
    vector<ll> v(n);

  
    ll mai = 0;
    for(int i =0; i<n; i++){
      cin>>v[i];  
      mai = max(mai,v[0]);
    } 
    
    set <ll> mods;
    for (ll i = 0; i<=60; i++){
        set <ll> mods;
        
        ll ind = pow(2,i);
        //cout<<"i: "<<i<<" | ind: "<<ind<<endl;
        
        for (int j = 0; j<n; j++){
            mods.insert(v[j]%ind);

            if (mods.size() > 2){
                break;
            }
        }
        //cout<<"_\n";
        //for(int x : mods) cout<<x<<endl;
        //cout<<"_\n";
        if (mods.size()==2){
            cout<<ind<<endl;
            return;
        }

    }

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;

    while(w--) solve();
}

/*


*/