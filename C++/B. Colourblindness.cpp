#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;cin>>t;
    for(int w= 0; w<t;w++){
        int n; cin>>n;

        string va,vb;
        cin>>va>>vb;
        int con = 0;
        for (int i =0;i<n;i++){
            if (va[i] != vb[i]){
                if (va[i] == 'R' || vb[i] == 'R'){
                    cout<<"NO"<<endl;
                    con =1;
                    break;
                }
                
            }
        }
        if (con == 0) cout<<"YES"<<endl;
    }
}