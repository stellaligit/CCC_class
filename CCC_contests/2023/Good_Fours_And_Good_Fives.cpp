#include <vector>
#include <iostream>
using namespace std;

int func(int n) {
    int ans = 0;
    int m = n/5;
    for (int i = 0; i <= m; i++) {
        if ((n - 5 * i) % 4 == 0) {
            ans += 1;
        }
    }

    return ans;
}

/*
int func(int n) {
    int m = n % 20;
    if (m == 1 || m == 2 || m == 3 || m == 6 || m == 7 || m == 11) {
        return(n/20);
    } else {
        return(n/20 + 1);
    }
}

*/

int main() {
    cout << func(21) << endl;
    cout << func(40) << endl;
    cout << func(11) << endl;
    cout << func(1000000) << endl;
}