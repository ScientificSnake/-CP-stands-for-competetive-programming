#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string outstring;
    
    long long n;

    cin >> n;
    // outstring = (string) n;
    std::stringstream ss;

    ss << n << ' ';

    while (n > 1)
    {
        
        // if (n == 1){
        //     break;
        // }
        if (n % 2 == 0){
            n = n/2;
        }
        else{
            n = 3 * n + 1;
        }
        ss << n << " ";
        // outstring += ' ';
        // outstring += (string) n;

    }
    cout << ss.str() << "\n";
}