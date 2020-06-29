#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // File variables - r/w
    ifstream fin ("shuffle.in");
    ofstream fout ("shuffle.out");

    // Read data
    int N, a, b, c;
    fin >> N;
    int movements[N], cows[N];
    for (int i = 0; i < N; i++) {
        fin >> movements[i];
    }
    for (int i = 0; i < N; i++) {
        fin >> cows[i];
    }

    // Alg
    for (int i = 0; i < 3; i++) {
        int temp[N];
        for (int p = 0; p < N; p++) {
            temp[p] = cows[movements[p]-1];
        }
        for (int p = 0; p < N; p++) {
            cows[p] = temp[p];
        }
    }

    for (int i = 0; i < N;) {
        fout << cows[i++] << "\n";
    }
    
    return 0;
}