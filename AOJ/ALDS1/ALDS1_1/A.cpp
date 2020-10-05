#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void print_vector_oneline(vector<int> A) {
  for (int i=0; i<A.size()-1; i++) {
    cout << A[i] << " ";
  }
  cout << A[A.size()-1] << endl;
}

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  print_vector_oneline(A);

  // insertion sort
  for (int i=1; i<N; i++) {
    int v = A[i];
    int j = i-1;

    while (j >= 0 && A[j] > v) {
      A[j+1] = A[j];
      j--;
    }
    A[j+1] = v;

    print_vector_oneline(A);
  }
}