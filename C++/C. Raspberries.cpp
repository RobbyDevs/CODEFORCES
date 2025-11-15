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
    
    vector<ll>vg;
    
    ll npar = 0;
    ll maig = 0;
    for(ll i = 0; i<n; i++){
        cin>>v[i];
        if (v[i]%2==0)npar++;
        vg.push_back(__gcd(v[i],k));
        maig = max(vg[vg.size()-1],maig);


    }

    if(k == 2){
        if(npar==0)cout<<1<<endl;
        else cout<<0<<endl;
    }
    
    if (k==4){
        if(npar>1 || maig == k)cout<<0<<endl;
        else if(npar==1)cout<<1<<endl;
        else{
            ll p3=0,p7=0;
            for(ll x:v){
                if(x==3)p3=1;
                if(x==7)p7=1;
            }

            if(p3+p7==0)cout<<2<<endl;
            else cout<<1<<endl;
            

        }
    }
    if(k==3 || k==5){
        if(maig == k)cout<<0<<endl;
        else{
            ll ans = 100;
            for(ll x:v){
                if(x>k){
                    ans = min(ans,(((x/k)+1)*k)-x);
                }
                else{
                    ans = min(ans,k-x);
                }
            }
            cout<<ans<<endl;
        }
        
    }

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