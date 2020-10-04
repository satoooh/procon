#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;

  int ans = 1;

  // ここにプログラムを追記
  for (int i = 1; i < S.size(); i += 2) {
    char si = S.at(i);
    if (si == '+') {
      ans += 1;
    }
    else {
      ans -= 1;
    }
  }

  cout << ans << endl;
}
