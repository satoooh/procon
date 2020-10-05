#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  double x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;

  double ans = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
  cout << fixed << setprecision(8) << ans << endl;
}