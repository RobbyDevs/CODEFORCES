#include<bits/stdc++.h>
using namespace std;

void solve(){

    int n;
    cin>>n;

    int ans = 1;
    for (int i = 0; i<n; i++){
        cout<<ans<<" ";
        ans+=2;
    }
    cout<<endl;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int w; cin>>w;
    while(w--)solve();
}