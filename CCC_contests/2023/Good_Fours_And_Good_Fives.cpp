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

/*
int func(int n) {
    int m = n/5;
    int r = n % 5;
    if (r == 1) {
        m -= 3;
    } else if (r == 2) {
        m -= 2;
    } else if (r == 3) {
        m -= 1;
    }
    if (m < 0) {
        return 0;
    } else {
        return m % 4 + 1;
    }
}

*/

int func(int n) {
    int m = n / 5;
    int r = n % 5;
    switch (r) {
        case 1: m--;
        case 2: m--;
        case 3: m--;
    }
    return m<0 ? 0 : (m%4)+1;
}

int func(int n) {
    int m = n / 5;
    int r = n % 5;
    if (r != 0 ) m -= (4-r);
     return m<0 ? 0 : (m%4)+1;
}

int main() {
    cout << func(21) << endl;
    cout << func(40) << endl;
    cout << func(11) << endl;
    cout << func(1000000) << endl;
}