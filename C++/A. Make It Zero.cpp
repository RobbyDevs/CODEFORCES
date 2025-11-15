#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n;
    cin>>n;
    vector <ll> v(n);

    ll sxor = 0;
    
    for (int i=0; i<n; i++){
        int a; cin>>a;
        sxor^=a;
        cout<<"+ "<<a<<"xor: "<<sxor<<endl;

        v[i] = a;

    }
    
    if (sxor == 0){
        cout<<"1\n";
        cout<<1<<" "<<n<<endl;
        return;
    }
    
    //sort(v.begin(),v.end());
    
    for (ll x : v) cout<<x<<" ";
    cout<<endl;
    cout<<sxor<<endl;

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
1
8
3 1 4 1 5 9 2 6

*/