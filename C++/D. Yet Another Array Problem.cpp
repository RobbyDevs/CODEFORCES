#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    //crivo
    ll n = 10010;
    vector<ll> primo(n, 1);
    primo[0] = 0;
    primo[1] = 0;
    
    ll p = 2;

    while (p*p <=n){
        if (primo[p]){
            for (ll i = p*p; i< n; i+=p)
                primo[i] = 0;
        }
        p++;
    }

    int t; cin>>t;
    for(int w = 0; w<t;w++){
        int nn;
        cin>>nn;

        vector<ll>v(nn);
        for(int i = 0; i<nn;i++)cin>>v[i];

        vector<ll> nprimos;

        for (ll i = 1; i<55; i++){
            if (primo[i]==1){
                nprimos.push_back(i);
            }
        }

        int flag = 0;
        for (int i = 0; i<17; i++){
            for (int j = 0; j<nn; j++){
                if (__gcd(v[j],nprimos[i]) == 1){
                    cout<<nprimos[i]<<endl;
                    flag = 1;
                    break;
                }
            }
            if (flag == 1) break;
        }

        if(flag == 0) cout<<-1<<endl;

    }

    return 0;
}

