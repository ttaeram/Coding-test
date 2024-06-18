#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int L{};
  cin>>L;
  string str{};
  cin>>str;

  long long r{1};
  long long M{1234567891};
  long long ans{0};

  for(int i=0; i<L; i++)
    {
      int res{long(str[i]) - 96};
      ans+=(res*r)%M;
      r=(r*31)%M;
    }
  cout<<ans%M;
}