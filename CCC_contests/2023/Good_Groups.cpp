#include <vector>
#include <iostream>
#include <map>
using namespace std;

int main() {
    int x;
    cin >> x;
    vector<vector<string>> same;
    for(int i = 0; i < x; i++) {
        vector<string> people;
        string a;
        cin >> a;
        people.push_back(a);
        cin >> a;
        people.push_back(a);
        same.push_back(people);
    }

    int y;
    cin >> y;
    vector<vector<string>> different;
    for(int i = 0; i < y; i++) {
        vector<string> people;
        string a;
        cin >> a;
        people.push_back(a);
        cin >> a;
        people.push_back(a);
        different.push_back(people);
    }

    int g;
    cin >> g;
    map<string, int> groups;
    for(int i = 0; i < g; i++) {
        string a;
        cin >> a;
        groups[a] = i;
        cin >> a;
        groups[a] = i;
        cin >> a;
        groups[a] = i;
    }

    int c = 0;

    for (auto item : same) {
        if (groups[item[0]] != groups[item[1]]) {
            c++;
        }
    }

    for (auto item : different) {
        if (groups[item[0]] == groups[item[1]]) {
            c++;
        }
    }

    cout << c;
    
    /*
    // map<string, int>::iterator it;
    for(auto it=groups.begin(); it!=groups.end(); ++it){
      cout << it->first << " => " << it->second << '\n';
    }
    */
   
    return 0;
}
