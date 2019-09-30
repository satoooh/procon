#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }

  int sum = 0;
  for (int i = 0; i < N; i++) {
    sum += A.at(i);
  }

  int ave = sum / N;

  for (int i = 0; i < N; i++) {
    int ans;
    if (A.at(i) >= ave) {
      ans = A.at(i) - ave;
    }
    else {
      ans = ave - A.at(i);
    }
    cout << ans << endl;
  }
}
