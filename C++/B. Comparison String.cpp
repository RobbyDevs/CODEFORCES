#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n;cin>>n;
    string v;
    set <int> vans;

    cin>>v;
    int mai = 1;
    int val = 0;
    int count = 1;
    char ant = v[0];

    for (int i = 1; i < n ; i++){
        if (v[i] == ant){
            count++;
            ant = v[i];         
            
        }else{
            mai = max(count,mai);
            count = 1;
            ant = v[i];
        }

    }
    mai = max(count,mai);

    cout<<mai+1<<endl;



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

<<>>
3

>><>><>

mai conex +1

6>5<6>5>4>3<4<5>4


*/