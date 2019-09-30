#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  // ここにプログラムを追記
  string graph_a = "A:";
  string graph_b = "B:";

  while (A > 0) {
    graph_a += "]";
    A--;
  }
  cout << graph_a << endl;

  while (B > 0) {
    graph_b += "]";
    B--;
  }
  cout << graph_b << endl;
}
