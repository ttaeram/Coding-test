#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int A{}, B{}, V{}, ans{};
  cin>>A>>B>>V;
  ans=(V-A)/(A-B);
  if((V-A)%(A-B)==0)
  {
    ans+=1;
  }
  else
  {
    ans+=2;
  }
  cout<<ans<<"\n";
}