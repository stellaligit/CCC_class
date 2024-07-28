#include <vector>
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> list;
    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        list.push_back(a);
    }
    int half = n/2;
    int ans = 0;
    for(int i = 0; i < half; i++) {
        if(list[i] == list[i+half]) {
            ans++;
        }
    }
    cout << ans * 2;
    return 0;
}