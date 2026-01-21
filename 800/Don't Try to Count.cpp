#include <bits/stdc++.h>
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t, n, m;
    cin >> t;
    while(t-- > 0){
        string x, s;
        
        cin >> n >> m;
        cin >> x;
        cin >> s;
        
        bool found = false;
        int i;
        for(i = 0;5>=i;i++){
            if (x.find(s) != string::npos) {
                found = true;
                break;
            }
            x += x;
        }
        
        if(found) cout << i << "\n";
        else cout << -1 << "\n";
    }
    return 0;
}