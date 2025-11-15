#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    int n,m,k;
    cin>>n>>m>>k;

    vector<int>vm(m);
    for(int i = 0; i<m; i++)cin>>vm[i];
    
    vector<int>vk(k);
    for(int i=0;i<k;i++)cin>>vk[i];

    map<int,int>sabe;

    if (n-k >=2)
        for(int i = 0; i<m;i++)
            cout<<0;
    else if(n-k <= 0)
        for(int i = 0; i<m;i++)
            cout<<1;
    else{
        
        for (int i = 0; i<k; i++){
            sabe[vk[i]] = 1;
        }

        for (int i = 0; i<m; i++){
            if (sabe[vm[i]]){
                cout<<0;
            }
            else
                cout<<1;
        }


    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    while(w--){
        solve();
        cout<<endl;
    }
}