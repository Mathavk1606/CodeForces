#include <bits/stdc++.h>
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t-- > 0){
        int ans = 0;
        
        for (int i = 0; i < 10; i++){
            string str;
            cin >> str;
        
            for(int j = 0;10>j;j++){
                if(str[j] == 'X'){
                    ans += min({i, j, 9-i, 9-j}) + 1;
                }
            }
        }
        
        cout << ans << "\n";
    }
    return 0;
}