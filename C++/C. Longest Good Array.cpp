#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll l,r;
    cin>>l>>r;

    ll i = (l+r)/2;
    ll x, e = 0, d = i;

    while(e<i){

        x = l + (i*(i+1))/2;
        //cout<<x<<endl;

        if (x>r){
            d = i;
            i = (e+d)/2;
        }
        else if (x<r){
            e = i;
            i = (e+d)/2;
        }
        
            else break;
    }

    cout<<i+1<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    while(w--)solve();
}


