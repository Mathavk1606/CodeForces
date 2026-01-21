#include <bits/stdc++.h>

using namespace std;

int solve() {
    int n, a, v;
    cin >> n >> a;
    int x = a + 1;
    int y = a - 1;
    int c1 = 0, c2 = 0;
    for (int i = 0; i < n; ++i) {
        cin >> v;
        if (abs(v - x) < abs(v - a)) {
            c1 += 1;
        } else if (abs(v - y) < abs(v - a)) {
            c2 += 1;
        }
    }
    return c1 > c2 ? x : y;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << '\n';
    }
    return 0;
}