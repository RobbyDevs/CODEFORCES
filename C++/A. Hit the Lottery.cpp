#include <bits/stdc++.h>
using namespace std;

int main(){
    long n,a,s,l,r;
    cin>>n;

    r = n/100;
    r+= (n%100)/20;
    r+= ((n%100)%20)/10;
    r+= (((n%100)%20)%10)/5;
    r+= (((n%100)%20)%10)%5;


    cout<<r<<endl;
    return 0;

}