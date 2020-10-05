#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;

  vector<double> x(n);
  for (int i=0; i<n; i++) {
    cin >> x[i];
  }
  vector<double> y(n);
  for (int i=0; i<n; i++) {
    cin >> y[i];
  }

  double d1 = 0;
  for (int i=0; i<n; i++) {
    d1 += abs(x[i] - y[i]);
  }
  cout << fixed << setprecision(5) << d1 << endl;

  double d2 = 0;
  for (int i=0; i<n; i++) {
    d2 += pow(x[i] - y[i], 2.0);
  }
  d2 = sqrt(d2);
  cout << d2 << endl;

  double d3 = 0;
  for (int i=0; i<n; i++) {
    d3 += pow(abs(x[i] - y[i]), 3.0);
  }
  d3 = pow(d3, 1.0/3.0);
  cout << d3 << endl;

  double dinf = 0;
  for (int i=0; i<n; i++) {
    dinf = max(dinf, abs(x[i] - y[i]));
  }
  cout << dinf << endl;
}