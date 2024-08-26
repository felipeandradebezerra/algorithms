// Author: Felipe Andrade

#include <iostream>

using namespace std;

int max(int *array, int size) {
  int total = array[0];
  for (int i = 1; i < size; i++) {
    if (array[i] > total) {
      total = array[i];
    }
  }
  return total;
}

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    int size;
    cin >> size;

    int *array = new int[size];
    for (int j = 0; j < size; j++) {
      cin >> array[j];
    }

    int maximo = max(array, size);
    cout << "Case " << i + 1 << ": \n" << maximo << endl;
    delete[] array;
  }

  return 0;
}
