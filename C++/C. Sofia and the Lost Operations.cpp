#include <bits/stdc++.h>
using namespace std;

void solve(){

    int n,i;
        map<int,int> dic;
        cin>>n;

        vector <int> va(n),vb(n);

        for (i=0;i<n;i++)cin>>va[i];

        for (i=0;i<n;i++){
            cin>>vb[i];
            if (vb[i] != va[i]) dic[vb[i]]++;
        }
        int m; cin>>m;
        vector <int> vd(m);
        for (i=0;i<m;i++){
            cin>>vd[i];
            dic[vd[i]]--;

        }
        int ult = vd[m-1];
        int flag = 0;
        for (auto i:vb){
            if (i==ult){
            flag = 1;
            break;
            }
        }

        if (flag == 1){
            for (auto i:dic){
                if (i.second >0){
                    flag = 0;
                    break;
                }
            }
        }

        if (flag==1)cout<<"YES\n";
        else cout<<"NO\n";
    }
    

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;cin>>t;
    while (t--) solve();
    return 0;
    
}