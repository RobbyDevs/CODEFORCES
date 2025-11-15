#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n;
    cin>>n;
    set<char>sx;
    deque<int>ve;
    deque<int>vd;
    string s;
    cin>>s;

    //Ve
    for (int i = 0; i<n; i++){
        sx.insert(s[i]);
        ve.push_back(sx.size());
    }

    //Vd
    sx.clear();
    for (int i = n-1; i>=0; i--){
        sx.insert(s[i]);
        vd.push_front(sx.size());
    }
    int ans = 0;
    for (int i = 0; i<n-1;i++){
        ans = max(ans,(ve[i]+vd[i+1]));
    }


    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    while(w--)solve();
}