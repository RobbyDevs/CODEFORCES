#include<bits/stdc++.h>
using namespace std;

int main(){
    string a,b;

    set<char>va;

    string v = "abcdefghijklmnopqrstuvwxyz";

    string line;

    getline(cin,line);

    for (char i :line){
        for (char j:v) if (i==j) va.insert(i);

    }
    cout<<va.size()<<endl;
    
    return 0;

}