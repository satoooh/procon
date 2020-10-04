#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  vector<int> ans;
  while (true) {
    int n, x;
    cin >> n >> x;
    if (n == 0 && x == 0) {
      break;
    } else {
      int count = 0;
      for (int i=1; i<n; i++) {
        for (int j=i+1; j<n+1; j++) {
          int k = x-i-j;
          if (j+1 <= k && k <= n) {
            count++;
          }
        }
      }
      ans.push_back(count);
    }
  }

  for (int i=0; i<ans.size(); i++) {
    cout << ans[i] << endl;
  }
}