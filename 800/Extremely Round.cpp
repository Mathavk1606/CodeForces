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
        int count = 0;
        
        count += min(n, 9);
        
        if(n >= 10) count += min((n/10), 9);
        
        if(n >= 100) count += min((n/100), 9);
        
        if(n >= 1000) count += min((n/1000), 9);
        
        if(n >= 10000) count += min((n/10000), 9);
        
        if(n >= 100000) count += min((n/100000), 9);
        
        cout<<count<<"\n";
    }
    return 0;
}
