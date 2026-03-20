using namespace std;
#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
	int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n, m, k;
        cin >> n >> m >> k;

        vector<int> vec(n); for (auto &x: vec) cin >> x;

        unordered_map<int, int> netChange = {};


        int bi;
        int ci;
        for (int i = 0; i < t; i++) {
            cin >> bi;
            cin >> ci;
            
            bi -= 1;

            if (netChange[bi])
            {
                netChange[bi] += ci;
            } else {
                netChange[bi] = ci;
            }
            if (netChange[bi] + vec[bi]) {
                netChange.clear();
            }
            
        }

        for(int i = 0; i < n; i++ ){
            if (netChange[i]){
                cout <<     
            }
        }
    }
}