#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n,k,x;
    
    cin>>n>>k>>x;

    ll min=0, max=0;
    
    min = ((1+k)*k)/2;
    max = ((n+n-k+1)*k)/2;
    
    //cout<<min<<"\n";
    //cout<<max<<endl;

    if (x >= min && x <= max)
        cout<<"YES\n";

    else
        cout<<"NO\n";

    
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin >>w;
    while(w--){
        solve();
    }
}

/*


*/