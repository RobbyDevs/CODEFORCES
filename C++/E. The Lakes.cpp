#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,-1,1};

ll dfs(vector<vector<pair<ll,ll>>> & mat,ll l,ll c){
    
    if(l<0 || c<0 || l>=mat.size() || c>=mat[0].size())return 0;

    if (mat[l][c].first == 0 || mat[l][c].second > 0LL) return 0;

    ll area = mat[l][c].first;
    mat[l][c].second = 1;

    for (int i = 0; i<4;i++){
        area+= dfs(mat,l+dx[i],c+dy[i]);
    }
    
    return area;
    


}

void solve(){

    ll n,m,ans = 0;
    cin>>n>>m;

    vector<vector<pair<ll,ll>>> mat (n, vector<pair<ll,ll>>(m));
    for (int i = 0; i<n; i++){
        for( int j =0; j<m;j++){
            cin>>mat[i][j].first;
        }
    }

    for (int i = 0; i<n;i++){
        for (int j=0;j<m;j++){
            if (mat[i][j].first != 0 && mat[i][j].second == 0){
                ans = max(ans,dfs(mat,i,j));
            }
        }
    }
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w;cin>>w;
    while(w--)solve();
}