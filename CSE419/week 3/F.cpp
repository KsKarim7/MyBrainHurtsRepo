#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        vector<int> v(n);
        for (int i = 0; i < n; i++)
            scanf("%d", &v[i]);

        int i = 0, j = n - 1;
        if (v.size() > 1)
        {
            int count = 0;
            while (i < j)
            {
                if (abs(v[i] - v[j]) <= 1)
                {
                    count++;
                    j--;
                }
                else
                {
                    i++;
                }
            }
            if (v.size() - count == 1)
            {
                printf("YES\n");
            }
            else
            {
                printf("NO\n");
            }
        }
        else
        {
            printf("YES\n");
        }
    }
    return 0;
}