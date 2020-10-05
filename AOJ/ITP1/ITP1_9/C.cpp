#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;

  vector<int> points(2, 0);

  for (int i=0; i<n; i++) {
    string s1, s2;
    cin >> s1 >> s2;
    if (s1 < s2) {
      points[1] += 3;
    } else if (s1 > s2) {
      points[0] += 3;
    } else {
      points[0]++;
      points[1]++;
    }
  }

  cout << points[0] << " " << points[1] << endl;
}