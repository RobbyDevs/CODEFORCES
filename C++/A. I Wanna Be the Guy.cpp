#include <bits/stdc++.h>
using namespace std;

int main(){
    long n,a,s,l;
    cin>>n;

    cin>>l;
    set<int> v;

    for (int i = 0; i<l;i++){
        cin>>s;
        v.insert(s);
    }
    cin>>l;

    for (int i = 0; i<l;i++){
        cin>>s;
        v.insert(s);
    }

    if(v.size() < n) cout<<"Oh, my keyboard!\n";
    else cout<<"I become the guy.\n";

    return 0;

}