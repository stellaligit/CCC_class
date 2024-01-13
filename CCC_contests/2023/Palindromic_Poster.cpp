#include <iostream>
#include <vector>
using namespace std;

void func(int n, int m, int r, int c) {
    vector<vector<char>> ret(n, vector<char>(m, 'a'));
    bool ok = true;
    int i, j;
    if (n != r || m != c) {
        if ((n == r && m % 2 == 0 && c % 2 == 1) ||
            (m == c && n % 2 == 0 && r % 2 == 1)) {
            ok = false;
        } else if (n == r) {
            if ((m-c) % 2 == 1) {
                ret[n-1][m/2] = 'b';
            }
            for (i = (m-c)/2; i > 0; i--) {
                ret[n-1][i-1] = 'b';
                ret[n-1][m-i] = 'b';
            }
        } else if (m == c) {
            if ((n-r) % 2 == 1) {
                ret[n/2][m-1] = 'b';
            }
            for (i = (n-r)/2; i > 0; i--) {
                ret[i-1][m-1] = 'b';
                ret[n-i][m-1] = 'b';
            }
        } else {
            for (i = r; i < n; i++) {
                ret[i][m-1] = 'b';
            }
            for (i = c; i < m; i++) {
                ret [n-1][i] = 'b';
            }
        }
    }

    if (ok) {
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                cout << ret[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "IMPOSIBLE";
    }
}