#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  vector<int> count(26, 0);
  string s;
  while (getline(cin, s)) {
    for (int i=0; i<s.length(); i++) {
      int ind = (int)(tolower(s[i]) - 'a');
      count[ind]++;
    }
  }

  for (int i=0; i<26; i++) {
    cout << (char)((int)('a') + i) << " : " << count[i] << endl;
  }
}