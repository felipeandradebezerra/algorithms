// This algorithm calculates the greatest common divisor (GCD) for pairs of integers across multiple test cases.
// Author: Felipe Andrade

#include <iostream>

using namespace std;

int mdc(int a, int b) {
  while (a % b != 0) {
    int r = a % b;
    a = b;
    b = r;
  }
  return b;
}

int main() {
  int n;
  cin >> n;
  bool first_case = true;

  for (int i = 0; i < n; i++) {
    int c;
    cin >> c;
    
    for (int j = 0; j < c; j++) {
      int a, b;
      cin >> a >> b;
      if (first_case) {
        cout << "Case " << i + 1 << ": \n";
        first_case = false;
      }
      cout << mdc(a, b) << endl;
    }
    first_case = true;
  }

  return 0;
}
