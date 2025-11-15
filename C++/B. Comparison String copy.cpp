#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n;cin>>n;
    string v;
    set <int> vans;
    vector <int> ans;

    cin>>v;
    int mai = 1;
    int val = 0;
    
    for (int i = 0 ; i<n; i++){

        if (v[i] == '>') mai++;
    }

    for (int i =0; i<n; i++){
        if (i ==0){
            if (v[i] == '>'){
                vans.insert(mai);
                ans.push_back(mai);
                vans.insert(mai-1);
                ans.push_back(mai-1);

                val = mai-1;

            }
            else{
                vans.insert(mai-1); // 5>4>3<4>3>2<3>2
                
                ans.push_back(mai-1);
                vans.insert(mai);   // 6>5>4<5>4>3<4>3
                                    // >><>><>
                
                ans.push_back(mai);
                val = mai;
            }
        }
        else{
            if (v[i] == '>'){
                val--;
                vans.insert(val);
                
                ans.push_back(val);
            }
            else{
                val++;
                vans.insert(val);
                
                ans.push_back(val);
            }
        }
    }
    for(auto x : ans) cout<<x;
    cout<<endl;
    
    cout<<vans.size()<<endl;

    



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


*/