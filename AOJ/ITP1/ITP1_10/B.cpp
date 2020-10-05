#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  double a, b, C;
  cin >> a >> b >> C;

  double rad = C * M_PI / 180.0;

  double S = a * b * sin(rad) / 2;
  double L = a + b + sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * cos(rad));
  double h = b * sin(rad);

  cout << fixed << setprecision(5) << S << endl;
  cout << fixed << setprecision(5) << L << endl;
  cout << fixed << setprecision(5) << h << endl;
}