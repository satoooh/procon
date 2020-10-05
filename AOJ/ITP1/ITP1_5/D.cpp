#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

void call(int i, int n) {
  int x = i;
  if ( x % 3 == 0 ) {
    cout << " " << i;
    if ( i < n ) {
      call(i+1, n);
      return;
    }
  } else {
    while ( x ) {
      if ( x % 10 == 3) {
        cout << " " << i;
        if ( i < n ) {
          call(i+1, n);
          return;
        }
      }
      x /= 10;
    }
    if ( i < n ) {
      call(i+1, n);
      return;
    }
  }
}

int main() {
  int n;
  cin >> n;
  int i = 1;
  call(i, n);
  cout << endl;
}