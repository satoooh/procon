#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  string x;
  while (true) {
    cin >> x;
    if (x == "0") {
      break;
    } else {
      ll ans = 0;
      rep(i, 0, x.length()) {
        ans += (ll)(x[i] - '0');
      }
      cout << ans << endl;
    }
  }
}