#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, a, b;
  cin >> x >> a >> b;

  // 1.の出力
  x++;
  cout << x << endl;

  // ここにプログラムを追記
  int ans_2 = x * (a + b);
  cout << ans_2 << endl;

  int ans_3 = ans_2 * ans_2;
  cout << ans_3 << endl;

  cout << ans_3 - 1 << endl;
}
