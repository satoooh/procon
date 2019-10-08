#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  int M = max(max(A, B), C);
  int m = min(min(A, B), C);

  cout << M - m << endl;
}
