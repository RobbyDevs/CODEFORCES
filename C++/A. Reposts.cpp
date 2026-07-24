#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<ll>vans;
void pg(map<string,vector<string>>&g){
    cout<<endl;
    for(auto x:g){
        cout<<x.first<<": ";
        for(auto y:x.second){
            cout<<y<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}
ll dfs(string p,map<string,vector<string>>&g,map<string,ll>&vis){
    //cout<<p<<" -> ";
    ll ans = 0;
    if(!vis[p]){
        //if (p!="polycarp")
        vis[p]=1;
        
        for(auto x : g[p]){
            ans =  max(ans,1 + dfs(x,g,vis));
        }
        //cout<<"--"<<endl;
    }
    return ans;
}

int main(){
    ll m; cin>>m;

    map<string,vector<string>>g;
    map<string,ll>vis;

    for(ll i=0;i<m;i++){
        string a,b,c;
        cin>>a>>c>>b;
        transform(a.begin(),a.end(),a.begin(),::tolower);
        transform(b.begin(),b.end(),b.begin(),::tolower);
        vis[a] = 0;
        vis[b] = 0;

        g[b].push_back(a);
    }
    //cout<<endl;
    //pg(g);

    ll ans = dfs("polycarp",g,vis);
    
    //cout<<endl;
    cout<<ans+1<<endl;

}

/*
8
b < polycarp
c < b
d < c
e < polycarp
f < e
g < f
h < g
i < h

*/