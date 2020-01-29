/*
ID: your_id_here
TASK: test
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

int populate(int n) {
  int answer = 0;
  if (n*(n+1)/2 % 2 == 0) {
    return n;
  } else {
    return 0;
  }
}

int main() {
  int n = 7;
  std::cout<<populate(n)<<"\n";
  return 0;
}