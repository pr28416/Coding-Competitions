#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <cstdlib>
#include <set>

using namespace std;

int main() {
    ifstream fin ("hoofball.in");
    ofstream fout ("hoofball.out");
    int N;
    fin >> N;
    int cows[N];
    for (int i = 0; i < N; i++) {
        fin >> cows[i];
    }

    map<int, int> pairs;
    for (int p1 = 0; p1 < N; p1++) {
        int p2 = 0;
        for (int i = 0; i < N; i++) {
            if (i == p1) continue;
            int a = abs(cows[i]-cows[p1]);
            int b = abs(cows[p2]-cows[p1]);
            if ((a == 0 || b == 0) || (a < b && i != p1)) {
                p2 = i;
            }
        }
        pairs[cows[p1]] = cows[p2];
    }

    // for (auto& i: pairs) {
    //     cout << i.first << "\t" << i.second << "\n";
    // }

    vector< set<int> > sets;
    for (int i: cows) {
        set<int> s;
        s.insert(i);
        int last = i;
        while (s.find(pairs[last]) == s.end()) {
            int e = pairs[last];
            s.insert(pairs[last]);
            last = e;
        }
        sets.push_back(s);
    }

    int i = 0;
    while (i < sets.size()-1) {
        set<int> temp;
        // TODO: Change to set difference
        for (int j: sets[i]) temp.insert(j);
        for (int j: sets[i+1]) temp.insert(j);
        if (temp == sets[i]) {
            sets.erase(sets.begin() + i+1);
        } else if (temp == sets[i+1]) {
            sets.erase(sets.begin() + i);
        } else {
            i += 1;
        }
    }

    for (set<int>& i: sets) {
        for (int j: i) {
            cout << j << " ";
        }
        cout << "\n";
    }

    return 0;
}

