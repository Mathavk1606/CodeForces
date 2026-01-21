#include <bits/stdc++.h>
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t-- > 0){
        int n;
        cin >> n;
        vector<int> v(n);
        loop(i,n) cin >> v[i];
        
        int cnt = 0;
        for(int i = 1; i < n; i++){
            if(v[i-1] % 2 == v[i] % 2){
                cnt++;
            }
        }
        
        cout << cnt << "\n";
    }
    return 0;
}
