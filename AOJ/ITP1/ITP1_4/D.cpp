#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;
  vector<ll> a(n);
  for (int i; i < n; i++) {
    cin >> a[i];
  }
  ll min_val = 1000000, max_val = -1000000, sum_val = 0;
  for (int i; i < n; i++) {
    min_val = min(min_val, a[i]);
    max_val = max(max_val, a[i]);
    sum_val += a[i];
  }
  cout << min_val << " " << max_val << " " << sum_val << endl;
}