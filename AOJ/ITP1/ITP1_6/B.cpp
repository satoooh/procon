#include <bits/stdc++.h>
#include <tuple>

using namespace std;
typedef long long ll;

#define rep(i, a, b) for (int i=(int)a; i<(int)b; i++)

int main() {
  // initialize
  vector< pair<char, int> > cards;
  rep(i, 1, 13+1) {
    pair<char, int> p('S', i);
    cards.push_back(p);
  }
  rep(i, 1, 13+1) {
    pair<char, int> p('H', i);
    cards.push_back(p);
  }
  rep(i, 1, 13+1) {
    pair<char, int> p('C', i);
    cards.push_back(p);
  }
  rep(i, 1, 13+1) {
    pair<char, int> p('D', i);
    cards.push_back(p);
  }

  // 出現する pair を除去
  int n;
  cin >> n;

  rep(i, 0, n) {
    char c;
    int v;
    cin >> c >> v;
    pair<char, int> p(c, v);
    cards.erase(remove(cards.begin(), cards.end(), p), cards.end());
  }

  rep(i, 0, cards.size()) {
    cout << cards[i].first << " " << cards[i].second << endl;
  }
}