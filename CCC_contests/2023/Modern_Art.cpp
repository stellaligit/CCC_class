#include <vector>
#include <iostream>
using namespace std;

int main() {
    int m, n, k;
    cin >> m >> n >> k;

    vector<int> rows(m, 0);
    vector<int> columns(n, 0);

    for(int i = 0; i < k; i++) {
        char a;
        cin >> a;
        int b;
        cin >> b;
        if(a == 'R') {
            if(rows[b-1] == 0) {
                rows[b-1] = 1;
            } else {
                rows[b-1] = 0;
            }
        } else {
            if(columns[b-1] == 0) {
                columns[b-1] = 1;
            } else {
                columns[b-1] = 0;
            }   
        }
    }

    int x = 0;
    for(int i = 0; i < m; i++) {
        if(rows[i] == 1) {
            x++;
        }
    }

    int y = 0;
    for(int i = 0; i < n; i++) {
        if(columns[i] == 1) {
            y++;
        }
    }

    int ans = x * n + y * m - 2 * x * y;
    std::cout << ans;
}