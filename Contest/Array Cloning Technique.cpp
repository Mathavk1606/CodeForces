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
        
        std::map<int,int> element_counts;
        
        for(int i = 0; i < n; i++){
            std::cin >> arr[i];
            element_counts[arr[i]]++;
        }
        
        int max_count = 0;
        int max_element = arr[0];
        
        for(auto& p : element_counts){
            if(p.second > max_count){
                max_count = p.second;
                max_element = p.first;
            }
        }
        
        int remaining = n - max_count;
        int num_of_ops = 0;
        int tmp_max_count = max_count;
        
        while(remaining > 0){
            int swaps = std::min(remaining, tmp_max_count);
            num_of_ops += 1 + swaps;  // 1 clone + swaps
            remaining -= swaps;
            tmp_max_count *= 2;
        }
        
        std::cout << num_of_ops << "\n";
    }
    
    return 0;
}