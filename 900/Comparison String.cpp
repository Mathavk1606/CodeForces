#include <bits/stdc++.h>
#define loop(i,j,n) for(int i = j;n>i;i++)

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin >> t;
    
    while(t-- > 0){
        int n;
        std::cin >> n;
        std::string s;
        std::cin >> s;
        
        int maxConsecutive = 1;
        int currentConsecutive = 1;
        
        loop(i, 1, n){
            if(s[i] == s[i-1]){
                currentConsecutive++;
                maxConsecutive = std::max(maxConsecutive, currentConsecutive);
            }
            else{
                currentConsecutive = 1;
            }
        }
        
        std::cout << maxConsecutive + 1 << "\n";
    }
    
    return 0;
}