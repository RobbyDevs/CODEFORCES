#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll ans = 0;


void dfs(map<char,vector<int>>& grafo, map<char,int>& mapa, char vertice ){
    
    if (mapa[vertice] == 0){
        mapa[vertice] = 1;
        
        for (char i : grafo[vertice]){
            dfs(grafo,mapa,i);
        }
        //cout<<vertice<<": "<<ans<<endl;
    }
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin >>w;
    while(w--){

        string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        map<char,vector<int>>grafo;

        map<char,int> mapa;
        // mapa[vertice][indice][foi_visitado]

        char m; cin>>m;
        ll n = m - '@';
       // cout<<n<<endl;
        string sv;  

        while (cin>>sv){
            if(sv.size()<=1) break;
            grafo[sv[0]].push_back(sv[1]);
            grafo[sv[1]].push_back(sv[0]);
        }
        
        ll nans = 0;
        for (int i = 0; i<n; i++){
            if(mapa[txt[i]]) continue;
            else ans+=1;
            dfs(grafo, mapa, txt[i]);

        }
        


        cout<<ans<<endl;
        cout<<endl;
    }

}

/*


*/