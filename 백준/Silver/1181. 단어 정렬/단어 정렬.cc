#include <iostream>
#include <algorithm>
using namespace std;

int sorting(string a, string b)
{
    if(a.length() == b.length())
    {
        return a<b;
    }
    else
    {
        return a.length()<b.length();
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int N{};
    cin>>N;
    
    string arr[20000]{};
    for(int i=0; i<N; i++)
    {
        cin>>arr[i];
    }
    
    sort(arr, arr+N, sorting);
    for(int i=0; i<N; i++)
    {
        if(arr[i] == arr[i-1])
        {
            continue;
        }
        cout<<arr[i]<<'\n';
    }
    return 0;
}