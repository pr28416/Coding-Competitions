/*
ID: your_id_here
TASK: test
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

std::string allSets[] = {};
int r = 0;
int c = 0;

int populate(int n) {
  int answer = 0;
  if (n*(n+1)/2 % 2 == 0) {
    int req = (n*(n+1))/4;

    // PART 1: Create the dp 2d array, set the values of each DP position
    int dp[n+1][req+1];
    for (int i = 0; i < n+1; i++) {
      for (int j = 0; j < req+1; j++) {
        dp[i][j] = -1;
      }
    }

    // PART 2: Starting from the bottom-right corner, create sets
    span();

  } else {
    return 0;
  }
}

void span(int dp[r][c], int node, int totalSum, int currentSet[]) {

  return;
}

int main() {
  std::ifstream fin ("subset.in");
  int n;
  fin >> n;
  std::cout<<n<<"\t"<<populate(n)<<"\n";
  return 0;
}