#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    
    vector<int> v(n);
    
    for(int i = 0; i < n; i++) cin >> v[i];
    
    bool is = false;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
              if((v[j]%v[i])%2==0){
                  cout<<v[i]<<' '<<v[j]<<endl;
                  return;
              }
        }
    }
    if(!is)cout<<-1<<endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    
    return 0;
}