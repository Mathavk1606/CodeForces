#include <bits/stdc++.h>
#define loop(i,n) for(int i=0;i<n;i++)
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t-- > 0){
        int n,a,b;
        cin >> n >> a >> b;
        if(a+b+2<=n || (a == b && a == n)) cout << "Yes" << "\n";
        else cout << "No" << "\n";
    }
    return 0;
}