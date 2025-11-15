#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve(){
    int n;
    cin>>n;
    vector<int>v(n+1);
    vector<int>dif;
    map<int,int>res;

    ll ans = 0;

    for(int i = 1; i<=n ; i++)cin>>v[i];

    for (int i = 1; i<=n; i++){
        res[v[i]-i] ++;
    }

    for(auto &item : res){
        //cout<<item.first<<"|"<<item.second<<endl;
        ll x = item.second;
        if (x > 1){
            ans += (((x-1)+1)*(x-1))/2;
        }
    }

    cout<<ans<<endl;

}


/*

1 6 3 4 5 6
0 4 0 0 0 0
*/

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--)solve();
}

