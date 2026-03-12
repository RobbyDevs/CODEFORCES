#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAXN 15

vector<vector<ll>>grid(1,vector<ll>(0));




//ajustar geralcao da grid
void pg(vector<vector<ll>>&grid){
        
    for(ll i=0;i<grid.size();i++){
        cout<<i<<": ";
        for (ll j = 0;j<grid[i].size();j++){
            cout<<grid[i][j]<<" ";
        }
        cout<<endl;
    }
    
}

void build(vector<vector<ll>>& grid){
    ll borda = MAXN;
    ll inicio = 1;
    ll nivel = 1;
    ll valor = 1;
    ll taml = 1;
    ll dif = 2;
    ll vdif =1;
    ll basehdif = 2;
    

    /*
    [ [] [0,1,3,6,10,15]
    [] [0,2,5]
    ]
    
    */
   while (taml >0){
        pg(grid);
        
        if (grid.size()<=nivel){
            grid.push_back(vector<ll>(1,0));
            grid[nivel].push_back(0);

        }
    

        if (nivel == 1)
            grid[nivel].push_back(1);

        else{
            grid[nivel].push_back(grid[nivel-1][0]+vdif);
            vdif++;
        }

        
        valor = grid[nivel].back();
        while (valor < borda){
            valor = grid[nivel].back() + dif;
            grid[nivel].push_back(valor);
            dif++;
        }
        taml = (grid[nivel].size()) - 2;
        borda-=1;
        nivel++;
        dif = nivel+1;
    }



}

void solve(){

}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;cin>>w;
    build(grid);
    while(w--)solve();
}
/*

1 3 6 10 15 ->5
2 5 9 14
4 


*/