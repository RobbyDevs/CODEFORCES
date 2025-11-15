#include <bits/stdc++.h>
using namespace std;

int main(){
    long a,b,n;
    cin>>n;
    vector <long> va(n);
    vector <long> vb(n);


    for (long i=0;i<n;i++){
        cin>>va[i];
        cin>>vb[i];
    }
    long c = 0;
    for (long i:va){
        for (long j:vb){
            if (i==j) c++;

        }
    }
    cout<<c<<endl;
    return 0;



}