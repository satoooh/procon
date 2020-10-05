#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  string str;
  while (true) {
    cin >> str;
    if (str == "-") {
      break;
    } else {
      int m;
      cin >> m;
      rep(i, 0, m) {
        int h;
        cin >> h;
        str = str.substr(h) + str.substr(0, h);
      }
      cout << str << endl;
    }
  }
}