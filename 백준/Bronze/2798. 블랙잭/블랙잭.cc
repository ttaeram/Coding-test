#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N{};
  int M{};
  int ans{0};

  cin>>N;
  cin>>M;

  int arr[N];
  for(int i=0; i<N; i++)
    {
      cin>>arr[i];
    }
  
  for(int i=0; i<N; i++)
    {
      for(int j=i+1; j<N; j++)
        {
          for(int k=j+1; k<N; k++)
            {
              int res{arr[i]+arr[j]+arr[k]};
              if(ans<res && res<=M)
                {
                  ans=res;
                }
            }
        }
    }
  cout<<ans;
}