#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N{}, maxa{-1};
  double ans{}, res{}, a{};
  cin>>N;

  for(int i=0; i<N; i++)
  {
    cin>>a;
    res+=a;
    if(maxa<a)
    {
      maxa=a;
    }
  }
  ans=((res/maxa)/N)*100;
  cout<<ans<<"\n";
}