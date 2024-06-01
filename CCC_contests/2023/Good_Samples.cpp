#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    // calculate if k is bigger than the max num of good samples possible
    // or less than minimum
    if (m >= n) {
        // when m>=n, max number is for sequence with no duplicated numbers.
        // ie. 1 2 3 .. n, which the total is: n+(n-1)+(n-2)...+2+1 == n * (n + 1))/2
        if (k > ((n * (n + 1))/2) || k < n) {
            cout << "-1";
            return 0;
        }
    } else {
        // when m<n, max layout is 1, 2, 3, .. m, 1, 2, 3,...m.
        // the total number is: (m * (n - m)) + (m * (m + 1))/2
        if (k > (m * (n - m)) + (m * (m + 1))/2 || k < n) {
            cout << "-1";
            return 0;
        }
    }

    // forming an array with each number being how many samples can be made
    // starting at that position from the composition we will be making.
    // for each position the number should be at least 1. which means 
    // the only good sample is it self. The next number is the same as it.
    // for instance:  1, 1, 1, 1, 1, the total number is n

    // for any position except the last position. we can add the number by 1
    // simply make it different to the next number. and the same as the one after
    // the next position. For instance, 1, 2, 1, 2, 1, the total number is n+(n-1)

    // similarly, we can increase any position except the last 2 by another 1,
    // simply make it different to the 2 next number. and the same as the 3rd next number
    // For instance, 1, 2, 3, 1, 2, 3, 1, the total number is n+(n-1)+(n-2)

    // x is calculating how many rows of "1"s since calculating total num of "1"s
    // so the total number should be n+(n-1)+(n-2)+...+(n-x+1)=(n+(n-x+1))*x/2
    // total = (-x*x+ (2n+1)x) / 2, the minimum integer x is the root of the formala
    // total >= k, => x*x-(2n+1)x + 2k <= 0
    int x = ((2 * n + 1) - sqrt((2 * n + 1) * (2 * n + 1) - 8 * k))/2;
    // a is the total number is all x rows have been filled with 1
    // if a>k, it means x should be greater than the root of the ...
    // if a==k, x is the root of the ...
    int a = (((2 * n + 1 - x)) * x) / 2;
    if (a != k) {
        x++;
        a = a + n - x + 1;
    }
    
    // y is the positions not filled fully with 1. for example
    // 1, 1, 1, 1, 1, ... , 1, 1, 1
    // 1, 1, 1, 1, 1, ... , 1, 1, 
    // 1, 1, 1, 1, 1, ... , 1, 
    // 1, 1, 1, 1, 1, ... ,
    // 0, 0, 1, 1, 1, ...
    // in this example, x is the total rows. y is 2. y is also a-k
    int y = a - k;

    // making the composition
    vector<int> s(n);
    int v = x;

    // for position from y to n, it's repeat of the full sequence.
    for (int i = n-1; i >= y; i--) {
        s[i] = v;
        if (--v == 0) {
            v = x;
        }
    }
    // for position from 0 to y-1, it's a repeat of full squences minus one number.
    // for instance, the
    // 1, 2, 3, 1, 2, 3, (no 4 before this position),  1, 2, 3, 4, 1, 2, 3, 4.... (y==6)
    // or 3, 4, 2, 3, 4, (no 1 before this position), 2, 3, 4, 1, 2, 3, 4.... (y==5)
    // or 3, 4, 1, 3, 4, 1, (no 2 before this position),  3, 4, 1, 2, 3, 4.... (y==6)
    // which means we remove the number should be at position y.z   
    int skip = v;
    if (--v == 0) {
        v = x;
    }
    for (int i = y - 1; i >= 0; i--) {
        s[i] = v;
        if (--v == 0) {
            v = x;
        }
        if (v == skip) {
            if (--v == 0) {
                v = x;
            }
        }
    }

    for (auto item:s) {
        cout << item << " ";
    }
    return 0;
}