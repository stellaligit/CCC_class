#include <iostream>
#include <vector>
#include <array>
#include <climits>

using namespace std;

int main() {
    // get input
    int n, m, r, c;
    cin >> n;
    cin >> m;
    cin >> r;
    cin >> c;

    vector<vector<char>> ret(n, vector<char>(m, 'a'));
    bool ok = true;

    int i, j;
    for (i=0; i<n-1; i++) {
        ret[i][m-1] = 'b';
    }
    for (i=0; i<m-1; i++) {
        ret[n-1][i] = 'b';
    }
    ret[n-1][m-1] = 'c';
    
    if (c<m && r<n) {
        for (i=0; i<c; i++) {
            ret[n-1][i] = 'a';
        }
        for (i=0; i<r; i++) {
            ret[i][m-1] = 'a';
        }
    } else if (c==m) {
        for (i=0; i<m-1; i++) {
            ret[n-1][i] = 'a';
        }
        ret[n-1][m-1] = 'b';
        if (n % 2 == 0 && r % 2 == 1) {
            ok = false;
        } else {
            if (r % 2 == 1) {
                ret[n/2][m-1] = 'a';
            }
            for (i=1; i<r; i+=2) {
                ret[i-1][m-1] = 'a';
                ret[n-i][m-1] = 'a';
            }
        }
    } else {
        // r == n
        for (i=0; i<n-1; i++) {
            ret[i][m-1] = 'a';
        }
        ret[n-1][m-1] = 'b';
        if (m % 2 == 0 && c % 2 == 1) {
            ok = false;
        } else {
            if (c % 2 == 1) {
                ret[n-1][m/2] = 'a';
            }
            for (i=1; i<c; i+=2) {
                ret[n-1][i-1] = 'a';
                ret[n-1][m-i] = 'a';
            }
        }
    }

    if (ok) {
        for (i=0; i<n; i++) {
            for (j=0; j<m; j++) {
                cout << ret[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "IMPOSSIBLE!";
    }
    return 0;
}