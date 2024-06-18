#include <iostream>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N{};
  cin>>N;

  int bee{1};
  int cnt{1};

  while(N>bee)
    {
      bee+=6*cnt;
      cnt+=1;
    }
  cout<<cnt;
}