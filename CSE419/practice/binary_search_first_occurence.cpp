#include <bits/stdc++.h>
using namespace std;

int first_occurence(int arr[], int n, int f)
{
    int s = 0;
    int e = n - 1;
    int res = -1;

    while (s <= e)
    {
        int mid = (s + e) / 2;

        if (arr[mid] == f)
        {
            res = mid;
            e = mid - 1;
        }
        else if (arr[mid] > f)
        {
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return res;
}
int main()
{
    int arr[] = {1, 2, 2, 2, 3, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int f;
    cin >> f;
    cout << first_occurence(arr, n, f);
    return 0;
}