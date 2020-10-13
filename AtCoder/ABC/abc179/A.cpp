#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  string S;
  cin >> S;
  char c = S[S.length()-1];
  if ( c != 's' ) {
    cout << S + "s" << endl;
  } else {
    cout << S + "es" << endl;
  }
}