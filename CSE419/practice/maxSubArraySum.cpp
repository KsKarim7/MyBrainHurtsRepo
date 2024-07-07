#include <iostream>
#include <vector>
#include <algorithm>

// Kadane's algorithm implementation

int maxSubArraySum(std::vector<int> &arr)
{
    int max_current = arr[0];
    int max_global = arr[0];

    for (int i = 1; i < arr.size(); i++)
    {
        max_current = std::max(arr[i], max_current + arr[i]);
        if (max_current > max_global)
        {
            max_global = max_current;
        }
    }

    return max_global;
}

int main()
{
    std::vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int max_sum = maxSubArraySum(arr);
    std::cout << "Maximum sum of a subarray: " << max_sum << std::endl;
    return 0;
}