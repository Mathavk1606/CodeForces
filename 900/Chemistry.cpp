#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i<n;i++)
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin >> t;
    while(t-->0){
        int n,k;
        std::cin >> n >> k;
        string s;
        std::cin >> s;
        
        map<char, int> freq;
        loop(i,n){
            freq[s[i]]++;
        }
        
        int odd_Freq = 0;
        for(auto p : freq){
            if(p.second % 2 != 0) odd_Freq++;
        }
        
        cout << (odd_Freq <= k+1 ? "Yes" : "No") << "\n";
    }
    return 0;
}