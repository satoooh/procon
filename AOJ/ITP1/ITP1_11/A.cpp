#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<int> roll_dice(vector<int> dice, char c) {
  vector<int> res(6);
  if (c == 'E') {
    res[0] = dice[3]; res[1] = dice[1]; res[2] = dice[0];
    res[3] = dice[5]; res[4] = dice[4]; res[5] = dice[2];
  } else if (c == 'N') {
    res[0] = dice[1]; res[1] = dice[5]; res[2] = dice[2];
    res[3] = dice[3]; res[4] = dice[0]; res[5] = dice[4];
  } else if (c == 'S') {
    res[0] = dice[4]; res[1] = dice[0]; res[2] = dice[2];
    res[3] = dice[3]; res[4] = dice[5]; res[5] = dice[1];
  } else if (c == 'W') {
    res[0] = dice[2]; res[1] = dice[1]; res[2] = dice[5];
    res[3] = dice[0]; res[4] = dice[4]; res[5] = dice[3];
  }
  return res;
}

int main() {
  vector<int> dice(6);
  for (int i=0; i<6; i++) {
    cin >> dice[i];
  }

  string commands;
  cin >> commands;

  for (int i=0; i<commands.length(); i++) {
    dice = roll_dice(dice, commands[i]);
  }

  cout << dice[0] << endl;
}