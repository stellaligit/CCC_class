#include <vector>
#include <iostream>
#include <map>
using namespace std;

int main() {
    int t, n;
    cin >> t >> n;
    vector<char> answers;
    for (int i = 0; i < t; i++) {
        map<char, int> comp;
        string a;
        cin >> a;

        for(auto letter : a) {
            if(comp.find(letter) != comp.end()) {
                comp[letter] = 1;
            } else{
                comp[letter] = 0;
            }
        }
        char prev, current;
        char ans = 'T';
        if(comp[a[0]] == 0) {
            current = 'L';
        } else {
            current = 'H';
        }        
        for(int i = 1; i < size(a); i++) {
            prev = current;
            if(comp[a[i]] == 0) {
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