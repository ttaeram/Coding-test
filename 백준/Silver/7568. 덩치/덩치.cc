#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N{};
    cin>>N;
    int arr[N*2];

    for(int i=0; i<N*2; i++)
    {
        cin>>arr[i];
    }

    for(int i=0; i<N*2; i+=2)
    {
        int cnt{1};
        for(int j=0; j<N*2; j+=2)
        {
            if(arr[i]<arr[j] && arr[i+1]<arr[j+1])
            {
                cnt+=1;
            }
        }
        cout<<cnt<<' ';
    }
}