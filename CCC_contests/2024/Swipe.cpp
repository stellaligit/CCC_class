#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> start;
    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        start.push_back(a);
    }
    vector<int> result;
    for(int i = 0; i < n; i++) {
        int b;
        cin >> b;
        result.push_back(b);
    }
    int count = 0;
    vector<vector<int>> swipes_left;
    vector<vector<int>> swipes_right;

    bool correct = true;
    int start_i = 0;
    int result_i = 0;
    while (start_i < n && result_i < n) {
        if(result[result_i] == start[start_i]) {
            int j = result_i;
            while(result[j] == start[start_i]) {
                j++;
                if (j == n) {
                    // succeed.
                    break;
                }
            }

            if (start_i < j - 1) {
                // operation: swipt right from start_i to j-1
                vector<int> right_swipe;
                right_swipe.push_back(1);
                right_swipe.push_back(start_i);
                right_swipe.push_back(j - 1);
                swipes_right.push_back(right_swipe);
                count++;
            }
            if (start_i > result_i) {
                // operation: swipt left from start_i to result_i
                vector<int> left_swipe;
                left_swipe.push_back(0);
                left_swipe.push_back(start_i);
                left_swipe.push_back(result_i);
                swipes_left.push_back(left_swipe);
                count++;
            }

            result_i = j;
        } else {
            // find next start_i matches result_i
            int k = start_i;
            while(start[k] != result[result_i]) {
                k++;
                if (k == n) {
                    // failed
                    correct = false;
                    break;
                }
            }
            start_i = k;
        }
    }

    if(correct) {
        cout << "YES" << endl << count << endl;

        // all in swipe_left
        // then, all in swipe_right but REVERSED.
        for(auto item : swipes_left) {
            cout << "L " << item[1] << ' ' << item[2] << endl;
        }

        for (int k=swipes_right.size()-1; k>=0; k--) {
            auto item = swipes_right[k];
            cout << "R " << item[1] << ' ' << item[2] << endl;      
        }
    } else {
        cout << "NO";
    }
}