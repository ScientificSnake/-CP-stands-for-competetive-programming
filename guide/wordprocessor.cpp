#include <cstdio>
#include <iostream>
#include <list>

using namespace std;

int main(){

    freopen("word.in", "r", stdin);
    freopen("word.out", "w", stdout);


    int n;
    int k;

    cin >> n >> k;

    string currentline;
    int currentlinechars;

    string newword;
    cin >> currentline;
    currentlinechars = currentline.length();

    for(int i=1; i < n; i++){
        cin >> newword;
        if (currentlinechars + newword.length() <= k){
            currentline += " " + newword;
            currentlinechars += newword.length();
        } else {
            cout << currentline << "\n";
            currentlinechars = newword.length();
            currentline = newword;
        }
    }

    cout << currentline; // last line

}