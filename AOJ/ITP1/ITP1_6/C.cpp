#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;

  vector< vector< vector<int> > > buildings(4, vector< vector<int> >(3, vector<int>(10, 0)));

  for (int i=0; i<n; i++) {
    int b, f, r, v;
    cin >> b >> f >> r >> v;
    buildings[b-1][3-f][r-1] += v;
  }

  for (int i=0; i<4; i++) {
    for (int j=0; j<3; j++) {
      for (int k=0; k<10; k++) {
        cout << " " << buildings[i][2-j][k];
      }
      cout << endl;
    }
    if (i != 3) {
      cout << string(20, '#') << endl;
    }
  }
}