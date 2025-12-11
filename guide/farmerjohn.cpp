#include <cstdio>
#include <iostream>
#include <list>

using namespace std;

int min(int *nums, int size);
int max(int arr[], int size);

int main()
{
	freopen("paint.in", "r", stdin);
	// the following line creates/overwrites the output file
	freopen("paint.out", "w", stdout);

    int a;
    int b;
    int c;
    int d;

    cin >> a >> b >> c >> d;

    int nums[4] = {a, b, c, d};
    int nums1[2] = {a, b};
    int nums2[2] = {c, d};

    int lowbound1 = min(nums1, 2);
    int highbound1 = max(nums1, 2);

    int lowbound2 = min(nums2, 2);
    int highbound2 = max(nums2, 2);

    if ((c <= highbound1 && c >= lowbound1) || (d <= highbound1 && d >= lowbound1)){        
        int minval = min(nums, 4);
        int maxval = max(nums, 4);

        cout << (maxval - minval) << "\n";
    }
    else if((a <= highbound2 && a >= lowbound2) || (b <= highbound2 && b >= lowbound2)){
        int minval = min(nums, 4);
        int maxval = max(nums, 4);

        cout << (maxval - minval) << "\n";
    }
    else { // no overlap
        int dist1 = abs(a-b);
        int dist2 = abs(c-d);

        cout << (dist1 + dist2) << "\n";
    }

}

int min(int* num, int size) {
    int min = num[0];
    // cout << "i=0 min=" << min << "\n";
    for (int i=1; i<size; i++){
        if (num[i] < min) min = num[i];
        // cout << "i=" << i << " min=" << min << "\n";
    }
    return min;
}

int max(int arr[], int size){
    int max = arr[0];
    // cout << "i=0 max=" << max << "\n";
    for (int i=1; i<size; i++){
        if (arr[i] > max) max = arr[i];
        // cout << "i=" << i << " max=" << max << "\n";
    }
    return max;
}
