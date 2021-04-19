#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime(int n) {
    if (n == 2 || n == 3 || n == 5) return true;
    else if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n < 2) return false;
    else {
        int s = sqrt(n)+1;
        for (int i = 3; i < s; i+=2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

int main() {
    vector<unsigned long long int> primes;
    for (int i = 2; i < 10000000; i++)
        if (isPrime(i)) {
            // cout << i << " ";
            primes.push_back(i);
        }

    // cout << "\n";
    unsigned long long int products[primes.size()-1];
    int prodSize = primes.size()-1;
    for (unsigned long long int i = 0; i < prodSize; i++) {
        unsigned long long int & a = primes[i];
        unsigned long long int & b = primes[i+1];
        products[i] = a*b;
    }

    // cout << "Finished\n";
    // for (unsigned long long int i = 0; i < 10; i++) {

    // }

    int T, Z;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> Z;
        int idx = upper_bound(products, products+prodSize, Z) - products;
        // int idx = 0;
        // while (idx < prodSize) {
        //     if (products[idx] > Z) {
        //         --idx;
        //         break;
        //     }
        //     ++idx;
        // }
        cout << "Case #" << t << ": " << products[idx-1] << "\n";
    }

    // for (auto i = primes.begin(); i != primes.end(); ++i)
    //     cout << *i << " ";
    // int T;
    return 0;
}