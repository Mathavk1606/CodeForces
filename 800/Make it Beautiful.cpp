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
        loop(i,n){
            cin >> v[i];
        }
        
        if(*max_element(v.begin(), v.end()) == *min_element(v.begin(), v.end())){
            cout << "No\n";
        }
        else{
            cout << "Yes\n";
            loop(i,n){
                if(i == 0) cout << v[n-1] << " ";
                else cout << v[i-1] << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}