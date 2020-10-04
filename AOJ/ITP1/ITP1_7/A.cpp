#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  vector<char> scores;
  while (true) {
    int m, f, r;
    cin >> m >> f >> r;
    if (m == -1 && f == -1 && r == -1) {
      break;
    } else {
      if (m == -1 || f == -1) {
        scores.push_back('F');
      } else if (m + f >= 80) {
        scores.push_back('A');
      } else if (m + f >= 65) {
        scores.push_back('B');
      } else if (m + f >= 50) {
        scores.push_back('C');
      } else if (m + f >= 30) {
        if (r >= 50) {
          scores.push_back('C');
        } else {
          scores.push_back('D');
        }
      } else {
        scores.push_back('F');
      }
    }
  }

  for (int i=0; i<scores.size(); i++) {
    cout << scores[i] << endl;
  }
}