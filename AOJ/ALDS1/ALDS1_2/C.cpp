#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  int N;
  cin >> N;
  vector<string> C(N);
  rep(i, 0, N) {
    cin >> C[i];
  }

  vector<string> C1(N); // for BubbleSort
  copy(C.begin(), C.end(), C1.begin());
  vector<string> C2(N); // for SelectionSort
  copy(C.begin(), C.end(), C2.begin());

  string s1 = "Stable"; // for BubbleSort
  string s2 = "Stable"; // for SelectionSort


  // BubbleSort
  rep(i, 0, N) {
    for (int j=N-1; j>i; j--) {
      if ((int)C1[j][1] < (int)C1[j-1][1]) {
        swap(C1[j], C1[j-1]);
      }
    }
  }

  // check stable or not
  rep(i, 0, N) {
    rep(j, i+1, N) {
      rep(a, 0, N) {
        rep(b, a+1, N) {
          if ( C[i][1] == C[j][1] && C[i] == C1[b] && C[j] == C1[a] ) {
            s1 = "Not stable";
            break;
          }
        }
      }
    }
  }

  rep(i, 0, N-1) {
    cout << C1[i] << " ";
  }
  cout << C1[N-1] << endl;
  cout << s1 << endl;


  // SelectionSort
  int minj;
  rep(i, 0, N) {
    minj = i;
    rep(j, i, N) {
      if (C2[j][1] < C2[minj][1]) {
        minj = j;
      }
    }
    if (i != minj) {
      swap(C2[i], C2[minj]);
    }
  }

  // check stable or not
  rep(i, 0, N) {
    rep(j, i+1, N) {
      rep(a, 0, N) {
        rep(b, a+1, N) {
          if ( C[i][1] == C[j][1] && C[i] == C2[b] && C[j] == C2[a] ) {
            s2 = "Not stable";
            break;
          }
        }
      }
    }
  }

  rep(i, 0, N-1) {
    cout << C2[i] << " ";
  }
  cout << C2[N-1] << endl;
  cout << s2 << endl;
}