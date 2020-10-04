#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  string S;
  getline(cin, S);

  for (int i=0; i<S.length(); i++) {
    if ( isupper(S[i]) ) {
      S[i] = tolower(S[i]);
    } else if ( islower(S[i]) ) {
      S[i] = toupper(S[i]);
    }
  }

  cout << S << endl;
}