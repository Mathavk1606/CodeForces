#include <bits/stdc++.h>
#define loop(i,j,n) for(int i = j;n>i;i++)

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin>>t;
    
    while(t-->0){
        int n,k;
        std::cin >> n >> k;
        
        std::vector<int> arr(n);
        
        loop(i,0,n) std::cin >> arr[i];
        
        std::sort(arr.begin(), arr.end());
        
        int i,j;
        i = 0;
        j = 1;
        int ans = INT_MIN;
        while(j<n){
            if(arr[j]-arr[j-1]<=k){ 
                j++;
            }
            else{
                ans = std::max(ans,j-i);
                i = j;
                j++;
            }
        }
        std::cout << ans << "\n";
    }

    return 0;
}