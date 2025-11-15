#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


void solve(){
    int a,b,n;
    cin >> a >> b >>n;
    vector <int> v(n);


    for (int i = 0; i<n; i++) cin>>v[i];

    sort(v.begin(),v.end());

    ll mai = b;
    int tempo = 0;

    for (int i = 0; i<n; i++){
        //cout<<b<<endl;
        if (v[i]+b <= a){
            b+=v[i];
            tempo+= b-1;
            b -=1;
        }
        else{
            tempo += b-1;
            b = a;
        }
        
        
        
        
        
        
    }
    cout<<tempo+1<<endl;
    

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;
    while(w--){
        solve();
    }
}


/*
so escolher as menores ferramentas e se na proxima ferramenta que for escolhida
o tempo passar de a, espere ficar menor ou igual a a, depois selecione. Faca
para todas as ferramentas

2 2 5
4 5 2 2 5
*/