#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n;
    cin>>n;

    ll soma=0;
    ll sp=0,si=0;
    vector<ll>v(n);

    for(ll i=0; i<n; i++){
        cin>>v[i];
        soma+=v[i];
        if(i%2!=0)sp+=v[i];
        else si+=v[i];
    }

    if(soma%n !=0)
        cout<<"NO"<<endl;

    else{
        //cout<<sp<<" "<<si<<endl;
        ll npar = n/2;
        ll nimp = n/2;
        if(n%2!=0) nimp++;
        //cout<<npar<<" "<<nimp<<endl;

        if(sp/npar == si/nimp )
            cout<<"YES"<<endl;

        else cout<<"NO"<<endl;

    }


}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin>>t;
    while(t--) solve();

}
/*

6 2 1 4 2

*/