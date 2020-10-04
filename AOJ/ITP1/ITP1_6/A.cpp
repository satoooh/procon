#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i=0; i<n; i++) {
    cin >> a[i];
  }

  cout << a[n-1];
  for (int i=1; i<n; i++) {
    cout << " " << a[n-i-1];
  }
  cout << endl;
}