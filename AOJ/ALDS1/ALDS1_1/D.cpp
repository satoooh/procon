#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int n;
  cin >> n;

  vector<ll> R(n);
  rep(i, 0, n) {
    cin >> R[i];
  }

  ll minv = R[0];
  ll maxv = R[1] - R[0];

  rep(j, 1, n) {
    maxv = max(maxv, R[j]-minv);
    minv = min(minv, R[j]);
  }

  cout << maxv << endl;
}