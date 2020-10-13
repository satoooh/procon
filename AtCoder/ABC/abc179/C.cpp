#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int N;
  cin >> N;

  // A * B + C == N
  // 1 <= A*B < N なる組 (A, B) のそれぞれに対して C = N - A*B と一意にとれる
  // よって A*B < N なる組 (A, B) の個数を求める問題に帰着

  int ans = 0;

  rep(A, 1, N) {
    // B の個数は 1, 2, ..., N//A だけ（ただし A*B == N に注意）
    ans += N/A;
    if (N%A == 0) {
      ans--;
    }
  }
  cout << ans << endl;
}