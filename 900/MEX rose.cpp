#include <bits/stdc++.h>
#include <algorithm>
#include <vector>
using namespace std;

int solve() {
    int n, k;
    cin >> n >> k;
    
    vector<int> v(n);
    for(int i = 0; i < n; i++) cin >> v[i];
    
    sort(v.begin(), v.end());
    
    set<int> s(v.begin(), v.end());
    
    int no_of_ks = count(v.begin(), v.end(), k);
    int ans = 0;
    
    for(int i = 0; i < k; i++){
        if(!s.count(i)){
            ans++;
        }
    }
    
    return max(no_of_ks,ans);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << "\n"; 
    }
    return 0;
}