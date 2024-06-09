#include <iostream>

using namespace std;
int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin>>n;
  int ans=0;
  int temp=0;
  int cnt=0;

  for(int i=0; i<n; i++)
    {
      cin>>temp;
      for(int j=1; j<=temp; j++)
      {
        if(temp%j==0)
          cnt++;
      }
      if(cnt==2)
        ans++;
      cnt=0;
    }
  cout<<ans<<'\n';
  return 0;
}