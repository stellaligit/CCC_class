#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    // get input
    int len;
    cin >> len;

    int * h = new int[len];
    int v;
    for (int i=0; i<len; i++) {
        cin >> v;
        h[i] = v;
    }

    int * r = new int[len];
    for (int i=0; i<len; i++) {
        r[i] = INT_MAX;
    }

    bool odd = true;
    int w;
    for (int i=0; i<len*2; i++) {
        int start = i / 2;

        int end;
        if (odd) {
            w = 0;
            end = start;
        } else {
            w = 1;
            end = start + 1;
        }

        int t = 0;
        for (int j=0; start-j>=0 && end+j<len; j++) {
            t += abs(h[start-j] - h[end+j]);
            if (r[w]>t) {
                r[w] = t;
            }
            w += 2;
        }

        odd = !odd;
    }

    for (int i=0; i<len; i++) {
        cout << r[i] << " ";
    }

    delete r;
    delete h;
}