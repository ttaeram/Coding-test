#include <iostream>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int N{}, K{};
    int N_{1}, K_{1}, NK{1};
    int ans{};
    
    cin>>N>>K;
    
    for(int n=1; n<N+1; n++)
    {
        N_ *= n;
    }
    
    for(int k=1; k<K+1; k++)
    {
        K_ *= k;
    }
    
    for(int nk=1; nk<N-K+1; nk++)
    {
        NK *= nk;
    }
    
    ans = N_/(NK * K_);
    cout<<ans<<'\n';
    return 0;
}