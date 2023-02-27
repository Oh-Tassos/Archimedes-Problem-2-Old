#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

int pow(int x, int y);
int cdigit(int x, int y);
void pfactorisation(int x);

std::vector<int> nfactors;
std::vector<int> nexps;

int main() {
    std::ofstream excel;
    excel.open("archimedes_p2_old.csv");
    excel << "N; Factors; n\n";
    
    for (int i = 1; true; ++i) {
        if ((cdigit(i, 5) == 1) && (cdigit(i, 2) > 0)) {
            int sr = sqrt(i);

            if (i == sr * sr) {
                pfactorisation(i);
                excel << i << ";";

                for (int j = 0; j < nfactors.size(); ++j) {
                    excel << nfactors[j] << "^" << nexps[j];
                    if (!(j == nfactors.size() - 1)) {
                        excel << " * ";
                    }
                }

                nfactors.clear();
                nexps.clear();
                excel << ";" << cdigit(i, 2) << "\n";
                std::cout << i << ", n = " << cdigit(i, 2) << "\n";
            }
        }
    }

    excel.close();

    return 0;
}

int pow(int x, int y) {
    int result = 1;

    for (int i = 0; i < y; ++i) {
        result = result * x;
    }

    return result;
}

int cdigit(int x, int y) {
    int total = 0;
    int i = 1;

    while (true) {
        if (x > pow(10, i)) {
            ++i;
        }

        else {
            break;
        }
    }

    for (int j = i; j > 0; --j) {
        int num1 = x/pow(10, j - 1);
        int num2 = x/pow(10, j);

        int num = num1 - 10*num2;

        if (num == y) {
            ++total;
        }
    }

    return total;
}

void pfactorisation(int x) {
    int i = 0;

    while (x % 2 == 0) {
        ++i;
        x = x/2;
    }

    if (!(i == 0)) {
        nfactors.push_back(2);
        nexps.push_back(i);
        i = 0;
    }

    for (int j = 3; !(j > sqrt(x)); j = j + 2) {
        while (x % j == 0) {
            ++i;
            x = x/j;
        }

        if (!(i == 0)) {
            nfactors.push_back(j);
            nexps.push_back(i);
            i = 0;
        }
    }
}