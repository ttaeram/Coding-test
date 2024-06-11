#include <iostream>

using namespace std;
int arr[6];
int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N{};
  int T{};
  int P{};
  int a{0}, b{0}, c{0};

  cin>>N;

  for(int i=0; i<6; i++)
    cin>>arr[i];

  cin>>T;
  cin>>P;

  for(int i=0; i<6; i++)
    if(arr[i]%T == 0)
      {
        a+=arr[i]/T;
      }
    else
    {
      a+=((arr[i]/T) + 1);
    }
  cout<<a<<"\n";
  b+=N/P;
  c+=N%P;
  cout<<b<<" "<<c<<"\n";
}