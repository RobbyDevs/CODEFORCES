#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int c = 1, s = 1;

    for (int i = 0; i < n - 1; i++) {
        if (v[i + 1] >= v[i]) {
            c++;
        } else {
            if (c > s) {
                s = c;
            }
            c = 1;
        }
    }

    cout << max(c, s) << endl;

    return 0;
}
