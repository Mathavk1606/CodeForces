#include <bits/stdc++.h>
#define loop(i,n) for(int i=0;i<n;i++)
int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t, n;
    std::cin >> t;
    while(t-- > 0){
        std::string str;
        std::cin >> n;
        std::cin >> str;
        int ans = 0;
        int dots = 0;
        
        int currdots = 0;
        
        for(int i = 0; i < n; i++){
            if(str[i] == '.'){
                dots++;
                currdots++;
                ans = std::max(ans, dots);
            }
            else{
                dots = 0;
            }
        }
        
        if(ans > 2){
            std::cout << 2 << "\n";
        }
        else{
            std::cout << currdots << "\n";
        }
    }
    return 0;
}