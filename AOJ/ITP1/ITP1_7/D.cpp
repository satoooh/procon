#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  int n, m, l;
  cin >> n >> m >> l;

  vector< vector<ll> > A(n, vector<ll>(m));
  for (int i=0; i<n; i++) {
    for (int j=0; j<m; j++) {
      cin >> A[i][j];
    }
  }

  vector< vector<ll> > B(m, vector<ll>(l));
  for (int i=0; i<m; i++) {
    for (int j=0; j<l; j++) {
      cin >> B[i][j];
    }
  }

  vector< vector<ll> > C(n, vector<ll>(l));
  for (int i=0; i<n; i++) {
    for (int j=0; j<l; j++) {
      for (int k=0; k<m; k++) {
        C[i][j] += A[i][k] * B[k][j];
      }
    }
  }

  for (int i=0; i<n; i++) {
    for (int j=0; j<l-1; j++) {
      cout << C[i][j] << " ";
    }
    cout << C[i][l-1] << endl;
  }
}