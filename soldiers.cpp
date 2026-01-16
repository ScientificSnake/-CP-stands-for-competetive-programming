#include <bits/stdc++.h>
using namespace std;

int main(){
    int k;
    int n;
    int w;
    cin >> k >> n >> w;

    int cost = k * (w*(w+1))/2

    if ((n - cost) < 0){
        cout << abs(n-cost);
    }
    else{
        cout << '0';
    }


    
}