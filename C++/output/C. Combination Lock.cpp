#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll sum(vector<ll>vsoma){
    ll soma=0;
    for(auto x:vsoma)soma+=x;
    return soma;
}


void solve(){
    ll n,x;
    cin>>n>>x;
    vector<ll>v(n);

    for(ll i = 0; i<n; i++)cin>>v[i];

    sort(v.rbegin(),v.rend());

    ll men = 10000000000;
    ll elem = 0;
    ll ind = 0;
    ll ans = 0;
    for(ll i=0; i<n; i++){

        if(v[i]>=x){
            ans+=1;
        }

        else{
            men = min(men,v[i]);
            elem++;
            if (elem*men >=x){
                ans++;
                men = 10000000000;
                elem = 0;
            }
        }

    }

    cout<<ans<<endl;


}




int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--)solve();
    return 0;
}


/*

4 10
4 2 1 3
4 3 2 1
*/