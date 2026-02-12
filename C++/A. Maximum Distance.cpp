#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll n;
    cin>>n;
    vector<ll>vx(n,0);
    vector<ll>vy(n,0);
    ll aux= 0;
    ll ans = 0;

    for(int i=0;i<n;i++) cin>>vx[i];
    for(int i=0;i<n;i++) cin>>vy[i];
    
    for(int i=0;i<n;i++){
        
        for(int j=i+1;j<n;j++){
            
            ll dx = vx[i]-vx[j];
            ll dy = vy[i]-vy[j];

            aux = dx*dx + dy*dy;

            ans = max(aux,ans);

        }
    }
    
    cout<<(ll) (ans)<<endl;
    


    return 0;
}