#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  rep(i, 0, N) {
    cin >> A[i];
  }

  int count = 0;

  // バブルソートによる昇順ソート
  bool flag = true;  // 逆の隣接要素が存在する
  while (flag) {
    flag = false;
    for (int j=N-1; j>=1; j--) {
      if (A[j] < A[j-1]) {
        swap(A[j], A[j-1]);
        flag = true;
        count++;
      }
    }
  }

  rep(i, 0, N-1) {
    cout << A[i] << " ";
  }
  cout << A[N-1] << endl;
  cout << count << endl;
}