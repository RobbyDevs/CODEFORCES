#include <bits/stdc++.h>
using namespace std;

int solve(vector<int>& resultados){
    int n, s=1;
    cin>>n;
    //cout<<resultados[n]<<endl;
    if(resultados[n] != 0) s=resultados[n];
    else {
        for(int i=2; i*i<=n; i++){
            if(n % i == 0){
                s+=i;
                if(n/i != i) s += n/i;
            }
        }
        resultados[n] = s;
    }

    //cout<<"s: "<<s<<endl;
    // cout<<n<<": ";
    if(s > n) cout<<"abundant"<<endl;
    else if(s < n) cout<<"deficient"<<endl;
    else cout<<"perfect"<<endl;
    return 0;
}

int main(){
    vector<int> resultados(1000010, 0);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--) solve(resultados);
    return 0;
}