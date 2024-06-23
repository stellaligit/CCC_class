#include <iostream>
#include <vector>
#include <array>
#include <climits>

using namespace std;

void func(int n, int m, int r, int c) {
    vector<vector<char>> ret(n, vector<char>(m, 'a'));
    bool ok = true;
    int i,j;
    if (r!=n || c!=m) {
        if ((r==n && m%2==0 && c%2==1) ||
            (c==m && n%2==0 && r%2==1)) {
            ok = false;
        } else if (r==n) {
            if ((m-c)%2==1) {
                ret[n-1][m/2] = 'b';
            }
            for (i=(m-c)/2; i>0; i--) {
                ret[n-1][i-1] = 'b';
                ret[n-1][m-i] = 'b';
            }
        } else if (c==m) {
            if ((n-r)%2==1) {
                ret[n/2][m-1] = 'b';
            }
            for (i=(n-r)/2; i>0; i--) {
                ret[i-1][m-1] = 'b';
                ret[n-i][m-1] = 'b';
            }
        } else {
            for (i=r; i<n; i++) {
                ret[i][m-1] = 'b';
            }
            for (i=c; i<m; i++) {
                ret[n-1][i] = 'b';
            }
        }
    }

    if (ok) {
        cout << n << " " << m << " " << r << " " << c << endl;
        for (i=0; i<n; i++) {
            for (j=0; j<m; j++) {
                cout << ret[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "IMPOSSIBLE!";
    }
}

int main() {
    // get input
    /*
    int n, m, r, c;
    cin >> n;
    cin >> m;
    cin >> r;
    cin >> c;
    */

    func(5, 4, 5, 4);
    cout << endl;

    func(5, 4, 3, 2);
    cout << endl;

    func(5, 4, 5, 2);
    cout << endl;

    func(5, 4, 5, 3);
    cout << endl;

    func(5, 3, 5, 2);
    cout << endl;

    func(5, 3, 5, 1);
    cout << endl;

    func(5, 4, 3, 4);
    cout << endl;

    func(5, 4, 4, 4);
    cout << endl;

    func(6, 4, 4, 4);
    cout << endl;

    func(6, 4, 3, 4);
    cout << endl;

}
