#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while(t--) {
        long long s, k, m;
        cin >> s >> k >> m;
        
        // Number of complete k-minute intervals
        long long num_flips = m / k;
        
        // Time since the last flip
        long long time_since_last_flip = m % k;
        
        // Amount of sand that was falling at the last flip
        // This is the minimum of s and k (how much sand fell in the previous interval)
        long long sand_at_last_flip = min(s, k);
        
        // If there was at least one flip
        if(num_flips > 0) {
            // Remaining sand from the last flip cycle
            long long remaining = sand_at_last_flip - time_since_last_flip;
            cout << max(0LL, remaining) << "\n";
        } else {
            // No flips occurred, initial sand is falling
            long long remaining = s - m;
            cout << remaining << "\n";
        }
    }
    
    return 0;
}