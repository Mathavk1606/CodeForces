#include <bits/stdc++.h>
#include <numeric>
#define loop(i,j,n) for(int i = j;n>i;i++)

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin>>t;
    
    // std::vector<int> lcm(50);
    
    // loop(i,1,50){
    //     lcm.push_back(std::lcm(i));
    // }
    
    while(t-->0){
        long long n;
		std::cin >> n;

		// Initialize i to 1, which will be used to find the maximum interval
		int i = 1;
		// Increment i until n is not divisible by i
		while (n % i == 0) // O(60)
			i++;
		// Output the size of the maximum interval
		std::cout << i - 1 << "\n";
    }

    return 0;
}