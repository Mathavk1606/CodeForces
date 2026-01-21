#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

void solve()
{
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    
    bool isLeftInclined = (n - k) < (k - 1);
    
    if (!isLeftInclined) {
        for (int i = 0; i < (k - 1); i++) 
            cout << "LEFT" << endl;
    
        for (int j = 0; j < n - 1; j++) {
            cout << "PRINT " << s[j] << endl;
            cout << "RIGHT" << endl;
        }
        cout << "PRINT " << s[n - 1] << endl;
    }
    else {
        for (int i = 0; i < (n - k); i++) 
            cout << "RIGHT" << endl;
        
        for (int j = n - 1; j > 0; j--) {
            cout << "PRINT " << s[j] << endl;
            cout << "LEFT" << endl;
        }
        cout << "PRINT " << s[0] << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    solve();

    return 0;
}