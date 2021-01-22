#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    int children[N];
    for (int i = 0; i < N; i++) cin >> children[i];
    size_t size = sizeof(children) / sizeof(children[0]);
    sort(children, children + size);

    int lo = 0, up = N-1, c = 0;
    while (lo < up) {
        if (children[lo] + children[up] <= X) {
            lo++;
        }
        up--; c++;
    }
    if (lo == up) c++;

    cout << c << "\n";

    return 0;
}