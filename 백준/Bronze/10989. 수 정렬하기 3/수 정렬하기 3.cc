/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int N{};
    cin>>N;
    int arr[10001]{0};
    int a{};
    
    for(int i=0; i<N; i++)
    {   
        cin>>a;
        arr[a] += 1;
    }
    
    for(int j=0; j<10001; j++)
    {   
        if(arr[j] != 0)
        {
            for(int k=0; k<arr[j]; k++)
            {
                cout<<j<<'\n';
            }
        }
    }
    
    return 0;
}