#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {

  while (true) {
    int n;
    cin >> n;
    if (n == 0) {
      break;
    } else {
      vector<double> s(n);
      double m = 0;
      for (int i=0; i<n; i++) {
        cin >> s[i];
        m += s[i];
      }
      m /= (double)n;
      double var = 0;
      for (int i=0; i<n; i++) {
        var += pow(s[i] - m, 2.0) / (double)n;
      }
      double std = sqrt(var);

      cout << fixed << setprecision(5) << std << endl;
    }
  }
}