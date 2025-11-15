#include <bits/stdc++.h>
using namespace std;

int main(){
    int t,w,i,n; cin>>t;

    for (w=0;w<t;w++){

        cin>>n;
        vector <int> v(n);
        for(i=0;i<n;i++) cin>>v[i];

        int p = 0;

        int flag = 0;
        while (p<=256){

            vector<int> vc(n);
            for (i=0;i<n;i++)vc[i] = v[i]^p;

            int c = 0;

            for (i=0;i<n;i++)c^=vc[i];
            if (c==0){
                flag = 1;
                break;
            }
            p++;

        }
        if (flag ==0) cout<<-1<<endl;
        else cout<<p<<endl;
        
        
    }
}