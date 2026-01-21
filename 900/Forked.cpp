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
        int a,b;
        std::cin >> a >> b;
        int xk,yk;
        std::cin >> xk >> yk;
        int xq,yq;
        std::cin >> xq >> yq;
        
        int ans = 0;
        
        vector<pair<int,int>> possible = {{-a,b},{-b,a},{a,b},{b,a},{a,-b},{b,-a},{-a,-b},{-b,-a}};
        
        set<pair<int,int>> kingMoves, queenMoves;
        
        for(auto p : possible){
            kingMoves.insert({xk + p.first, yk + p.second});
            queenMoves.insert({xq + p.first, yq + p.second});
        }
        
        for(auto move : kingMoves){
            if(queenMoves.count(move)) ans++;
        }
        
        std::cout << ans << "\n";
    }
    return 0;
}