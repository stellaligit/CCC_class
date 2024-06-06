#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(vector<long> a, vector<long> b) {
    return (a[0] < b[0]);
}

int main() {
    long n;
    cin >> n;
    vector<vector<long>> data;
    for (long i=0; i<n; i++) {
        long p, w, d;
        vector<long> item;
        cin >> p >> w >> d;
        item.push_back(p);
        item.push_back(w);
        item.push_back(d);
        data.push_back(item);
    }

    sort(data.begin(), data.end(), comp);

    for (auto item : data) {
        cout << item[0] << " " << item[1] << " " << item[2] << endl;
    }

    long total = 0;
    long pConcert = data[0][0];
    for (long i=1; i<n; i++) {
        vector<long> item = data[i];
        if (item[0] - item[2] <= pConcert && pConcert <= item[0] + item[2]) {
            continue;
        }

        long delta = pConcert < item[0] ? 1 : -1;
        long newP = pConcert;
        long newTotal = 0;

        while (true) {
            newP += delta; 
            for(int j = 0; j <= i; j++) {
                int p = data[j][0];
                int w = data[j][1];
                int d = data[j][2];
                if (newP<=p+d && newP>=p-d) {
                    continue;
                }
                newTotal += (abs(newP - p) - d) * w;
            }
            // if newTotal <
        }

    }


}