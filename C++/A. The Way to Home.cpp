#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dfs(ll pos,string &v,ll d){
    
    ll nx = pos+d;

    for(ll i=nx;i>pos;i--){
        if((i>=0 && i<v.size()) && (v[i]=='1')){
            //cout<<i<<endl;
            return i;
        }
    }

    return 0;
}

int main(){
    ll n,d;
    cin>>n>>d;

    string v;
    cin>>v;

    ll ans = 0;
    ll pos = 0;

    while (pos<n-1)
    {   
       // cout<<pos<<endl;
        ll temp = dfs(pos,v,d);
        if (temp) ans+=1;
        else{
            ans = 0;
            break;
        }

        pos=temp;

    }
    if(ans)
    cout<<ans<<endl;
    
    else
    cout<<-1<<endl;

}