#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  string w;
  getline(cin, w);

  int ans = 0;

  string t;
  while (cin >> t) {
    if (t == "END_OF_TEXT") {
      break;
    }
    std::transform(t.begin(), t.end(), t.begin(), ::tolower);
    if (t == w) {
      ans++;
    }
  }

  cout << ans << endl;
}