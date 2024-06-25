#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  string N{}, Z{};
  while(1)
  {
    cin>>N;
    Z=N;
    reverse(N.begin(), N.end());
    if(N=="0")
      break;
    else if(N==Z)
      cout<<"yes"<<"\n";
    else
      cout<<"no"<<"\n";
  }
}