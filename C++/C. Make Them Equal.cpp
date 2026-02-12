#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(){
    ll n = 0;
    char c;

    cin>>n>>c;

    string v;
    cin>>v;

    vector<int>ans;
    bool flag = true;
    

    for(auto x:v){
        if (x!=c){
            flag = false; 
        }
    }

    if(!flag){
        for(int i = 1; i<n+1;i++){
            flag = true;

            for(int j = i; j<n+1;j++){
                flag &= (v[j-1]==c);
                j +=i-1;
            }
            if(flag){
                ans.push_back(i);
                break;
            }
        }


        if (!flag){
            ans.push_back(n);
            ans.push_back(n-1);
        }
    }
    cout<<ans.size()<<endl;
    for (auto x:ans){
        cout<<x<<" ";
    }
    cout<<endl;

}

int main(){
    ll w;cin>>w;
    while (w--)
        solve();
}