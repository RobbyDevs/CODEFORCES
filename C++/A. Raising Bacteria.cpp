#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ll n;cin>>n;
    ll ans = 0;
    ll p = 0;
    while (n>0){
        for(ll i=0;i<32;i++){
            if((1<<i)>n)break;

            else
                p=i;
            
        }
        n = (n-(1<<p));
        ans++;
    }
    cout<<ans<<endl;
}
