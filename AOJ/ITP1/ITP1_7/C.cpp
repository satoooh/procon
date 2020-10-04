#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int r, c;
  cin >> r >> c;

  vector< vector<int> > ans(r+1, vector<int>(c+1, 0));

  for (int i=0; i<r; i++) {
    for (int j=0; j<c; j++) {
      cin >> ans[i][j];
      ans[i][c] += ans[i][j];
      ans[r][j] += ans[i][j];
      ans[r][c] += ans[i][j];
    }
  }

  for (int i=0; i<r+1; i++) {
    for (int j=0; j<c; j++) {
      cout << ans[i][j] << " ";
    }
    cout << ans[i][c] << endl;
  }
}