#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int* h = new int[n];
    for(int i = 0; i < n; i++)
    {
        cin >> h[i];
    }

    int* maxV = new int[n];
    for(int i = 0; i < n; i++)
    {
        maxV[i] = INT_MAX;
    }

    for(int i = 0; i < n; i++)
    {
        cout << i << " : " << h[i] << '\t' << maxV[i] << endl;
    }

    delete h;
    delete maxV;
}