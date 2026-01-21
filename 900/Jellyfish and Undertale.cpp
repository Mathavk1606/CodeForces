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
        int a,b,n;
        std::cin >> a >> b >> n;
        vector<int> x(n);
        
        int ans = b;
        
        loop(i,n){
            std::cin >> x[i];
            ans += min(x[i],a-1);
        }
        
        std::cout << ans;
    }
    return 0;
}