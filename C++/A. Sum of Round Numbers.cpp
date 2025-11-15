#include <bits/stdc++.h>
using namespace std;

typedef long long lint;

int main(){
    lint t; cin>>t;

    for (int w=0; w<t; w++){
        string mess; cin>>mess;

        int c= 0;

        for (int i =0;i<mess.size();i++) if (mess[i]!='0')c++;
        cout<<c<<endl;

        
        for (int i = mess.size()-1; i>-1; i--){
            if (mess[i]!='0'){
                cout<<mess[i];

                int tam = ((mess.size()-1)-i);
                

                for (int j = 0; j<tam;j++) cout<<0;
                cout<<" ";
            }
        }
        cout<<endl;
        
    }
}

//9876
//
// 6 e 0 0s, porque o indice dele - n-1 == 0
//7 e 1 0 porque o indice dele - n-1 == 1
// ou seja, n de zeros == (indice - (n-1))


