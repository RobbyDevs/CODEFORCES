#include <bits/stdc++.h>

using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,l;
    cin>>n>>l;
    
    vector<double>v(n);
    for (int i = 0; i<n; i++) cin>>v[i];

    sort(v.begin(),v.end());

    double dif = 2*max(v[0],l-v[n-1]);

    for (int i = 0; i<n-1; i++)
        dif = max(dif,v[i+1]-v[i]);


    printf("%.10f\n",dif/2.);



}

/*

15 5 3 7 9 14 0
0 3 5 7 9 14 15


0 1 2 3 4 5
    2     5

*/