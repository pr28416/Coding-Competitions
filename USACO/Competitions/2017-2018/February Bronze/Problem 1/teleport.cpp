#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
    ifstream fin ("teleport.in");
    ofstream fout ("teleport.out");

    int st, en, tl1, tl2;
    fin >> st >> en >> tl1 >> tl2;
    fout << min(min(abs(en-st), abs(st-tl1)+abs(en-tl2)), abs(st-tl2)+abs(en-tl1)) << "\n";


    return 0;
}