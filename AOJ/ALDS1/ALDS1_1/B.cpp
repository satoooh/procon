#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int x, y;
  cin >> x >> y;

  // x > y に揃える
  if (x < y) {
    swap(x, y);
  }

  int tmp;
  while (x % y != 0) {
    tmp = x;
    x = y;
    y = tmp % y;
  }

  cout << y << endl;
}