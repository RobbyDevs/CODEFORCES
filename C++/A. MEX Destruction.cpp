#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void solve(){

    int n;
    cin>>n;
    vector<int>v(n);

    int ans = 0;
    for (int i =0;i<n;i++)cin>>v[i];

    if (v[0]!=0) ans++;

    for (int i = 1; i<n; i++){
        if (v[i]!=0 && v[i-1]==0)  ans++;
    }

    cout<<min(2,ans)<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w; cin>>w;
    while(w--)solve();
}