#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll NEG = -1e9;


void pg(vector<vector<ll>>&g){
  
  for(ll i=0;i<g.size();i++){
    cout<<i<<"("<<g[i].size()<<") "<<" : ";
    for(auto x:g[i])cout<<x<<" ";
    cout<<endl;
  }
  cout<<"-----"<<endl;
  cout<<endl;
}



ll dfs(ll p, vector<vector<ll>>& g){
  
  ll soma = 0;
  
  if (g[p].size() == 0)
    return 1;
    
  else if(g[p].size()<3)
    return NEG;
    
  else{
    for (auto x:g[p])
      soma += dfs(x,g);

    if (soma >=3)
      return 0;
      
  return NEG;
  
  }
  
  
}

int main(){ 
  
  ll n;cin>>n;
  
  vector<vector<ll>>g(n+1);

  for(ll i = 1; i<n;i++){
    ll aux; cin>>aux;
    g[aux].push_back(i+1);
  }
  
  //pg(g);
  ll ans = dfs(1,g);
  //cout<<ans<<endl;
  
  if (ans>=0)
    cout<<"YES"<<endl;
  else
    cout<<"NO"<<endl;
}