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

  // 選択ソートによる昇順ソート
  int minj;
  rep(i, 0, N) {
    minj = i;
    rep(j, i, N) {
      if (A[j] < A[minj]) {
        minj = j;
      }
    }
    if (i != minj) {
      swap(A[i], A[minj]);
      count++;
    }
  }

  rep(i, 0, N-1) {
    cout << A[i] << " ";
  }
  cout << A[N-1] << endl;
  cout << count << endl;
}