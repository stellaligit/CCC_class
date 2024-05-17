#include <vector>
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> heights;
    for(int i = 0; i <= n; i++) {
        int a;
        cin >> a;
        heights.push_back(a);
    }
    vector<int> widths;
    for(int i = 0; i < n; i++) {
        int b;
        cin >> b;
        widths.push_back(b);
    }

    double ans = 0;
    for(int i = 0; i < n; i++) {
        ans += ((heights[i] + heights[i + 1]) * widths[i]);
    }

    ans /= 2.0;
    cout << ans;

    return 0;
}