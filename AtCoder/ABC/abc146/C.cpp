#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

ll digit(ll N) {
  return log10(N)+1;
}

ll price(ll A, ll B, ll N) {
  return A*N + B*digit(N);
}

int main() {
  ll A, B, X;
  cin >> A >> B >> X;

  // 二分探索
  ll m = 1;
  ll M = 1e9;

  if (price(A, B, M) < X) {
    cout << M << endl; // 上限
  } else if(price(A, B, m) > X) {
    cout << 0 << endl; // 下限
  } else {
    ll mid = (m + M)/2;
    while (mid != m && mid != M) {
      if (price(A, B, mid) > X) {
        M = mid;
        mid = (m+M)/2;
      } else {
        m = mid;
        mid = (m+M)/2;
      }
    }
    cout << mid << endl;
  }
}