#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N{};
  int ans{0};
  cin>>N;

  for(int i=1; i<N; i++)
    {
      int res{0};
      int n{i};
      while(n!=0)
        {
          res+=n%10;
          n/=10;
        }
      
      if(i+res==N)
        {
          ans=i;
          break;
        }
    }
  cout<<ans;
  return 0;
}