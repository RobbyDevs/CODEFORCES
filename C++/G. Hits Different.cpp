#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAXN 1000010

vector<vector<pair<ll,ll>>> grid(1);;

vector<ll> vans(MAXN+10);

void pg(vector<vector<pair<ll,ll>>>&grid){
        
    for(ll i=0;i<grid.size();i++){
        cout<<i<<": ";
        for (ll j = 0;j<grid[i].size();j++){
            cout<<grid[i][j].first<<" ";
        }
        cout<<endl;
    }
    
}
void pv (vector<ll>&vans){
    for(auto x:vans)
        cout<<x<<" ";
    cout<<endl;
}
void build(vector<vector<pair<ll,ll>>>& grid){
    ll borda = MAXN;
    ll nivel = 1;
    ll valor = 1;    ll taml = 1;
    ll dif = 2;      ll vdif =1;
    
    while (taml >0){
        
        if (grid.size()<=nivel){
            grid.push_back(vector<pair<ll,ll>>());
            grid[nivel].push_back({0,0});
        }
    
        if (nivel == 1)
            grid[nivel].push_back({1,1});

        else{
            grid[nivel].push_back({grid[nivel-1][1].first+vdif,grid[nivel-1][1].first+vdif});
            vdif++;
        }

        valor = grid[nivel].back().first;
        while (valor < borda){
           
            valor = grid[nivel].back().first + dif;
            grid[nivel].push_back({valor,valor});
            dif++;
        }
        taml = (grid[nivel].size()) - 2;
        borda-=1;
        nivel++;
        dif = nivel+1;
    }
}

void prefix2d(vector<vector<pair<ll,ll>>>&grid,vector<ll>&vans){
    ll n = grid.size();
    for(ll i=0;i<n;i++)
        for(ll j=1;j<grid[i].size();j++)
            grid[i][j].first = grid[i][j-1].first+grid[i][j].first*grid[i][j].first;
        
    n = grid[1].size();
    for(ll j=1;j<n;j++)
        for(ll i=2;i<=n-j;i++)
            grid[i][j].first = grid[i-1][j].first + grid[i][j].first;
    
    for(auto x:grid)
        for(auto y:x)
            vans[y.second] = y.first;
}

void solve(vector<ll>&vans){
    ll n;cin>>n;
    cout<<vans[n]<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    build(grid);
    prefix2d(grid,vans);
    while(w--)solve(vans);
}
