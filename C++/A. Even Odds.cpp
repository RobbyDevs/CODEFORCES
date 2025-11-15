#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int main(){
    lint n,k;
    cin>>n>>k;

    
    lint im = n/2;
    if (n%2 !=0) im++;

    if (k<=im) cout<<(2*k)-1<<endl;
    else{
        k = k-im;
        cout<<2*k<<endl;
        
    }

    //1 2 3 4 5 6 7
    //1 3 5 7
    //2 4 6

// p == n//2
// if n par, i == p
// else i == p+1

//i-esimo i == (2*k-1)
//ex:  5.o i == 2*5-1 => 9

}