#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    string v;
    cin>>v;
    ll n = v.size();

    vector<string> vs = {"00","50","25","75"};

    ll ans = 100;
    ll ind = n;

    for (string x : vs){
        ll c = 0;
        char a = x[0];
        char b = x[1];

        for(ll i=n-1; i>0; i--){
            if (v[i] == b){
                ind = i;
                break;
            }
            else
            c++;
        }

        if (ind == n)continue;

        else{
            for(ll i=ind-1; i>=0; i--){
                if (v[i]==a){
                    break;
                }
                else
                c++;
            }
        }

        ans = min(ans,c++);
        //cout<<c<<endl;

    }
    cout<<ans<<endl;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin>>w;
    while(w--)solve();
}

/*
7 1 3 4 5

*/