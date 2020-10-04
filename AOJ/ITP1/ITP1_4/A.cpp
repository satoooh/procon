#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  ll a, b;
  cin >> a >> b;
  ll d = a/b, r = a%b;
  double f = (double)a/(double)b;
  cout << d << " " << r << " ";
  cout << fixed << setprecision(5) << f << endl;
}