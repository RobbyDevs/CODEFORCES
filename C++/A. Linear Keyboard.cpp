#include <bits/stdc++.h>

using namespace std;

void solve(){
    
    string alf;
    cin>>alf;
    string s;

    map<char,int> dic;
    int ans = 0;

    for (int i=1;i<alf.size()+1;i++){
        dic[alf[i-1]] = i;

    }

    
    cin>>s;
    int ant = dic[s[0]];

    for (int i =0; i< s.size();i++){
        ans+= abs(dic[s[i]]-ant);
        ant = dic[s[i]];
    }
    
    cout<<ans<<endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int w; cin>>w;
    while(w--){
        solve();
    }
}