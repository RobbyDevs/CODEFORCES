#include <bits/stdc++.h>
using namespace std;

int main(){
    int t; cin>>t;
    
    for (int w=0;w<t;w++){

        int n; cin>>n;

        int ind =1, ans = 0;

        while (ind<=n){
            for (int i=1;i<10;i++){
                if (ind*i <= n)ans++;
                else break;
                
            }
            ind = ind*10;
        }
        
        cout<<ans<<endl;
    }
    
}