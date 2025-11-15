#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n;cin>>n;

    vector < int> v(n);
    set <int> ks;

    int val;
    for (int i = 0; i< n; i++){
        cin>>val;
        if (val != i+1){
            ks.insert(abs(val-(i+1)));
        }
    }
    
    int mmc = 0;
    for (int x:ks) mmc = __gcd(mmc,x);

    cout<<mmc<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;

    while(w--){
        solve();
    }
}


/*

*/