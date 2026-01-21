#include <iostream>
#include <algorithm>
#include <climits>

#define loop(i,n) for(int i=0;i<n;i++)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n,x,t;
    std::cin >> t;
    while(t-->0){
        std::cin>>n>>x;
        int arr[n];
        loop(i,n){
            std::cin>>arr[i];
        }
        
        int answer = arr[0];  
        
        loop(i,n-1){
            answer = std::max(answer, arr[i+1] - arr[i]);
        }
        
        answer = std::max(answer, 2 * (x - arr[n-1]));
        
        std::cout << answer << "\n";
    }
    return 0;
}