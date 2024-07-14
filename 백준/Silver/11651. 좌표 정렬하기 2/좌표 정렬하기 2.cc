#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

struct position
{
    int x{};
    int y{};
};

bool compare(const position& now, const position& last)
{
    if(now.y != last.y)
    {
        return now.y < last.y;
    }
    else
    {
        return now.x < last.x;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N{};
    cin>>N;
    position arr[100001];

    for(int i=0; i<N; i++)
    {
        cin>>arr[i].x>>arr[i].y;
    }

    sort(arr, arr + N, compare);

    for(int i=0; i<N; i++)
    {
        cout<<arr[i].x<<' '<<arr[i].y<<'\n';
    }
}