#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  string s, p;
  getline(cin, s);
  getline(cin, p);
  s = s + s;
  if (s.find(p) != string::npos) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}