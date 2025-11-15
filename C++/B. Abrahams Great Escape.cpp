#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n, k ;
    cin>>n>>k;

    ll tam = n*n;
    
    if (tam-k == 1){
        cout<<"NO\n";
    }
    else{
        cout<<"YES\n";
        for (int i  = 0; i<n; i++){
            for (int j = 0; j<n;j++){
                if (k){
                    cout<<"U";
                    k--;
                }
                else{
                    // nao base

                    if (i<n-1){
                        cout<<"D";

                    }
                    else{
                        if (j<n-1)
                            cout<<"R";
                        else{
                            cout<<"L";
                        }
                        
                    }
                    
                }


            }
            cout<<endl;
        }


    }
    
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll w; cin >>w;
    while(w--){
        solve();
    }
}

/*


*/