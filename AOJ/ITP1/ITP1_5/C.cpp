#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  while (true) {
    int h, w;
    cin >> h >> w;
    if (h == 0 && w == 0) {
      break;
    } else {
      rep(i, 0, h) {
        rep(j, 0, w) {
          if ((i+j)%2 == 0) {
            cout << '#';
          } else {
            cout << '.';
          }
        }
        cout << endl;
      }
      cout << endl;
    }
  }
}