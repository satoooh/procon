#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  vector<int> a, b;
  while (true) {
    int x, y;
    cin >> x >> y;
    if (x == 0 && y == 0) {
      break;
    } else {
      a.push_back(x);
      b.push_back(y);
    }
  }
  for (int i=0; i < a.size(); i++) {
    cout << string(b[i], '#') << endl; // 最初の行
    for (int j=1; j < a[i]-1; j++) {
      cout << '#' + string(b[i]-2, '.') + '#' << endl;
    }
    cout << string(b[i], '#') << endl; // 最後の行
    cout << endl;
  }
}