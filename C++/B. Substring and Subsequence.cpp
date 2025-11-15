#include <bits/stdc++.h>

using namespace std;

void solve(){
    string a,b;

    cin>>a>>b;
    int ans = a.size()+b.size();

    for (int i = 0; i<b.size(); i++){
        int pont = i;
        for (int j = 0; j<a.size();j++){
            if (pont < b.size() && a[j] == b[pont]){
                pont +=1;
            }
        }
        int tam = a.size()+b.size();

        if (tam - pont+i < ans)
            ans = tam-pont+i;
        
    }

    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;
    while(w--){
        solve();
    }
}