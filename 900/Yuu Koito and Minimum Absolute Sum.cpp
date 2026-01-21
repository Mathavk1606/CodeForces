#include <iostream>
#include <map>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin >> t;
    
    while(t-- > 0){
        int n;
        std::cin >> n;
        int arr[n];
        
        for(int i = 0; i < n; i++){
            std::cin >> arr[i];
        }
        
        if(arr[0] == -1 && arr[n-1] == -1){
            arr[0] = arr[n-1] = 0;
        }
        else if(arr[0] == -1){
            arr[0] = arr[n-1];
        }
        else if(arr[n-1] == -1){
            arr[n-1] = arr[0];
        }
        
        std::cout << abs(arr[0] - arr[n-1]) << "\n";
        
        for(int i = 0; i < n; i++){
            if(arr[i] == -1) std::cout << 0 << " ";
            else std::cout << arr[i] << " ";
        }
        
        std::cout << "\n";
    }
    
    return 0;
}