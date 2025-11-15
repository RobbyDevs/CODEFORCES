#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){

    int armz=0,ans=0, t,a;
     
    int n; cin>>n;
    
     
    for (int i=0;i<n;i++){
        cin>>a;
        if (a>0) armz+=a;
        else{
            if (armz<=0) ans++;
            else armz--;
        }
    }
    cout<<ans<<endl;
    
}

//if armz <=0 unt ++


