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

  int r{31};
  int M{1234567891};
  int ans{0};

  for(int i=0; i<L; i++)
    {
      int res{str[i] - 96};
      ans+=res*(pow(r, i));
    }
  cout<<ans;
}