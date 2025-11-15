#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    lint t;cin>>t;

    for (lint w=0;w<t;w++){
        lint a,b,x,y,ans=0;
        cin>>a>>b>>x>>y;

        lint yy,xx;
        
        if (y<b)cout<<-1<<endl;
        else{
            a+= y-(b);
            ans +=y-(b);
            
            
            
            if (x>a)cout<<-1<<endl;
            else{
                ans += abs(a-x);
                cout<<ans<<endl;
            }

    

        }
    }
    return 0;
}
