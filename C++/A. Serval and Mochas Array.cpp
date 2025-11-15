#include <bits/stdc++.h>
using namespace std;




int main(){
    
    int t; cin>>t;

    for (int w=0; w<t; w++){
        int n; cin>>n;
        vector <int> v(n);
        for(int i=0;i<n;i++) cin>>v[i];
        int con = 0;
        for (int i =0;i<n;i++){
            for (int j=0;j<n;j++){
                if (i!=j){
                    if (__gcd(v[i],v[j])<=2){
                        con = 1; break;
                    }
                }
            }
            if (con == 1)break;
        }

        if (con == 1) cout<<"YES\n";
        else cout<<"NO\n";

    }
    return 0;
}

//
