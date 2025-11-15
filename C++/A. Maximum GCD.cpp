#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n;cin>>n;

    if (n%2 ==0)
        cout<<n/2<<endl;
    
    else cout<<(n-1)/2<<endl;



}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;

    while(w--){
        solve();
    }
}
