#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n,k;
    cin>>n>>k;

    ll a=0,b=0,c=0;
    string v;
    cin>>v;

    for(ll i=0; i<k;i++){
        if(v[i]=='0')a++;
        if(v[i]=='1')b++;
        if(v[i]=='2')c++;
    }

    string vans(n,'+');

    for(ll i = 0; i<n;i++){
        if (i < a+c || i >= n-b-c) vans[i] = '?';
        if (i < a || i >= n-b || k == n) vans[i] = '-';
    }

    cout<<vans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--)solve();
}