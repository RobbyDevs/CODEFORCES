#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll vy[3]= {-1,0,+1};

bool dfs(ll i,vector<char>& va , vector<char>& vb){

    if (va[i] == '1')      
        for(ll x=0; x<3; x++){

            ll ny = i + vy[x];

            if (ny>=0 && ny<vb.size()){
                
                if (vb[ny]=='0' && x==1){
                    vb[ny]='2';
                    return true;
                }

                if (vb[ny]=='1' && x!=1){
                    vb[ny] = '2';
                    return true;
                }

            }
        }

    return false;

}

void solve(){
    ll n;
    cin>>n;
    string linha;
    vector<char>va(n),vb(n);

    cin>>linha;
    for(ll i=0;i<n;i++)vb[i]=linha[i];

    cin>>linha;
    for(ll i=0;i<n;i++)va[i]=linha[i];
    
    ll ans = 0;

    for(int i =0;i<n;i++)
        if(va[i]=='1')
            if (dfs(i,va,vb)) ans++;
    
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin>>w;
    while(w--)solve();
}