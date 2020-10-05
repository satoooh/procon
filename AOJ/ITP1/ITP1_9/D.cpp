#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  string str;
  cin >> str;
  int q;
  cin >> q;

  string command;
  int a, b;
  string p;

  for (int i=0; i<q; i++) {
    cin >> command >> a >> b;

    // operation
    if (command == "print") {
      for (int i=a; i<=b; i++) {
        cout << str[i];
      }
      cout << endl;
    } else if (command == "reverse") {
      for (int i=a; i<=a+(b-a)/2; i++) {
        char tmp = str[i];
        str[i] = str[b-(i-a)];
        str[b-(i-a)] = tmp;
      }
    } else if (command == "replace") {
      cin >> p;
      for (int i=a; i<=b; i++) {
        str[i] = p[i-a];
      }
    }
  }
}