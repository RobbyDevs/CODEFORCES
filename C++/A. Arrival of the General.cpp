#include <bits/stdc++.h>
using namespace std;

int main() {
    long n, imai=0,imen = 1000000,mai=0,men = 10000000,ans=0;


    cin>>n;
    for (int i=0;i<n;i++){
        long a;
        cin>>a;
        if (a>mai){
            mai = a;
            imai = i;
        }
        if (a<=men){
            men = a;
            imen = i;
        }

    }
    //cout<<imai<<" "<<imen<<endl;
    ans = imai + ((n-1)-imen);
    if (imai>imen) ans--;

    cout<<ans<<endl;
    return 0;

}