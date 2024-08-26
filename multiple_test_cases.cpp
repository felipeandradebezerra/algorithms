// This algorithm processes multiple test cases, where each case consists of a series of events.
// Author: Felipe Andrade

#include <iostream>

using namespace std;

int main() {
    int total;
    cin >> total;

    for (int event = 1; event <= total; event++) {
        int f;
        cin >> f;

        cout << "Case " << event << ":\n";

        if (f == 0) {
            cout << "Empty case!" << endl;
        } else {
            for (int row = 1; row <= f; row++) {
                int a, b, c;
                cin >> a >> b >> c;

                int sum = a + b + c;
                cout << sum << endl;
            }
        }
    }

    return 0;
}
