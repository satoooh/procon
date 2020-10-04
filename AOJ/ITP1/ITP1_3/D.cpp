#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int count = 0;
  for (int i = a; i < b+1; i++) {
    if (c%i == 0) {
      count++;
    }
  }
  cout << count << endl;
}