#include "string"
#include "iostream"
using namespace std;

int main() {

    int barnlocationX = 0;
    int barnlocationY = 0;

    int lakeLocationX = 0;
    int lakeLocationY = 0;

    int rockLocationX = 0;
    int rockLocationY = 0;

    int targetLocationX = 0;
    int targetLocationY = 0;

    char targetChar;

    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            cin.get(targetChar);
            if (targetChar == 'B'){
                barnlocationX = j;
                barnlocationY = i;
                // std::cout << "barn at " << rock
            }
            else if (targetChar == 'L')
            {
                lakeLocationX = j;
                lakeLocationY = i;
            }
            else if (targetChar == 'R')
            {
                rockLocationX = j;
                rockLocationY = i;
            }
        }
    }

    int xdist = abs(barnlocationX - lakeLocationX) - 1;
    int ydist = abs(barnlocationY - lakeLocationY) - 1;

    if ((xdist == 0) || (ydist == 0)){
        // special case here
    } else {
        cout << xdist + ydist - 1;
    }
}