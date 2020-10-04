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
    for (int j=0; j < a[i]; j++) {
      cout << string(b[i], '#') << endl;
    }
    cout << endl;
  }
}