#include <iostream>

#include <iterator>
#include <vector>
using namespace std;

int main() {
    std::vector<string> closeplanets = {"Mercury", "Venus", "Earth","Mars"};

    // for (int i = 0; i < closeplanets.size(); i++) {
    //     cout << closeplanets[i] << endl;
    // }

    // ranged base for loop

    for(vector<string>::iterator it = closeplanets.begin(); it != closeplanets.end(); ++it) {
        cout << it << endl;
    }

    return 0;
}