#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
        cin >> n;
        string v;
        cin >> v;

        bool flag = false;
        for (int i = 0; i < n && !flag; i++) {
            for (int j = i + 1; j < n; j++) {
                if (v[i] == v[j]) {
                    if (i % 2 != j % 2) {
                        flag = true;
                        break;
                    }
                }
            }
        }

        if (flag)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin>>t;
    while(t--) solve();

}