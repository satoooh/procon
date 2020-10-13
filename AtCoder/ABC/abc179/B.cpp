#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int N;
  cin >> N;
  vector<int> D1(N), D2(N);

  string ans = "No";
  int count = 0;
  rep(i, 0, N) {
    cin >> D1[i] >> D2[i];
    if (D1[i] == D2[i]) {
      count++;
      if (count == 3) {
        ans = "Yes";
      }
    } else {
      count = 0;
    }
  }

  cout << ans << endl;
}