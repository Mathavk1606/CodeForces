#include <iostream>
#define loop(i,j,n) for(int i = j;n>i;i++)

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin >> t;
    
    while(t-- > 0){
        int n;
        std::cin >> n;
        
        if(n == 2 || n == 3) 
            std::cout << n << "\n";
        else
            std::cout << n%2 << "\n";
    }
    
    return 0;
}