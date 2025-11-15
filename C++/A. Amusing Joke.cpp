#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    map<char,int> dic;
    map<char,int> dic2;

    string a,b,v;

    cin>>a>>b>>v;

    for (auto i:a)dic[i]+=1;
    for (auto i:b)dic[i]+=1;
    for (auto i:v)dic2[i]+=1;
    if (dic == dic2) cout<<"YES\n";
    else cout<<"NO\n";
    return 0;

}