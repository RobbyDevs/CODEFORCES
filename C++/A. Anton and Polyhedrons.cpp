#include<bits/stdc++.h>
using namespace std;

int main(){
    string a,b;

    unordered_map <string,long> dic{{"Tetrahedron",4},{"Cube",6},{"Octahedron",8},{"Dodecahedron",12},{"Icosahedron",20}};

    long n; cin>>n;
    long ans = 0;
    for (long i = 0; i<n;i++){
        string a; cin>>a;
        ans += dic[a];

    }

    cout<<ans<<endl;
    return 0;

}