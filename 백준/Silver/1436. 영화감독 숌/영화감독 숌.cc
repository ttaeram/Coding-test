#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int tya(string a)
{
    int l{};
    l = a.length();
    for(int i=0; i<l-2; i++)
    {
        if(a[i] == '6' && a[i+1] == '6' && a[i+2] == '6')
        {
            return 1;
        }
    }
    return 0;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int N{};
    cin>>N;
    
    int movie{666};
    while(N>0)
    {
        string a{to_string(movie)};
        if(tya(a) == 1)
        {
            N -= 1;
            if(N == 0)
            {
                break;
            }
        }
        movie += 1;
    }
    cout<<movie<<'\n';
    
    return 0;
}