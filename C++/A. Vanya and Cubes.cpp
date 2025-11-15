#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void solve(){

    ll n;
    cin>>n;

    ll ans = 1;
    ll soma = 0;
    vector<ll>v;
    
    for (int i = 1; i<n+1; i++){
        soma+=i;
        v.push_back(soma);
    }
    soma = 0;
    for (int i = 0; i<n; i++){
        soma +=v[i];

        if (soma>n){
            cout<<i<<endl;
            return;
        }
        else if (soma == n){
            cout<<i+1<<endl;
            return;
        }
    }

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    //int w; cin>>w;
    solve();
}