#include <vector>
#include <iostream>
#include <map>
using namespace std;

int main() {
    int t, n;
    cin >> t >> n;
    vector<char> answers;
    for (int i = 0; i < t; i++) {
        int count[26];
        for (int j=0; j < 26; j++) {
            count[j] = 0;
        }

        string a;
        cin >> a;

        for(auto letter : a) {
            count[letter - 'a'] ++;
        }
        char prev, current;
        char ans = 'T';
        if(count[a[0]-'a'] == 1) {
            current = 'L';
        } else {
            current = 'H';
        }
        for(int i = 1; i < size(a); i++) {
            prev = current;
            if(count[a[i]-'a'] == 1) {
                current = 'L';
            } else {
                current = 'H';
            }

            if(current == prev) {
                ans = 'F';
                break;
            }
        }
        answers.push_back(ans);
    }
    for(auto item : answers) {
        cout << item << endl;
    }
    return 0;
}