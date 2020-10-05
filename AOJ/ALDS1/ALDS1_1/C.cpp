#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


// エラトステネスの篩
vector<bool> IsPrime;

void sieve(ll max){
  if (max+1 > IsPrime.size()) {
    IsPrime.resize(max+1, true);
  }
  IsPrime[0] = false;
  IsPrime[1] = false;

  for (ll i=2; i*i<=max; ++i) {
    if (IsPrime[i]) {
      for (ll j=2; i*j <= max; ++j) {
        IsPrime[i*j] = false;
      }
    }
  }
}


int main() {
  int n;
  cin >> n;

  sieve(100000000);

  int count = 0;
  for (int i=0; i<n; i++) {
    int x;
    cin >> x;
    if (IsPrime[x]) {
      count++;
    }
  }

  cout << count << endl;
}