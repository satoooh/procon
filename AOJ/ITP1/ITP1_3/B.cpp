#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int count = 1;
  while (true) {
    int x;
    cin >> x;
    if (x == 0) {
      break;
    } else {
      cout << "Case " << count << ": " << x << endl;
      count++;
    }
  }
}