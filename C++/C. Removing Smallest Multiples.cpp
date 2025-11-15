#include <bits/stdc++.h>
using namespace std;
void solve() {

    int n;
    cin>>n;
    string s;
    cin>>s;
    vector<int>v(n+1);

    for (int i = 0; i<n;i++) v[i+1]=s[i];
    long long ans = 0;
    v[0] = 1;
    
    for (int i = 1; i<=n; i++){

        for (int j = i; j<=n; j+=i){
            if (v[j] == '0'){
                ans+=i;
                v[j] = '-';
            }
            else{
                if(v[j] == '1'){
                    break;
                }

            }
        }
    }
    cout<<ans<<endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;
    cin>>w;
    while (w--) solve();
}