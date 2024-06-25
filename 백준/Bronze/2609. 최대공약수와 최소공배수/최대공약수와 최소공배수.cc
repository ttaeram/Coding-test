#include <iostream>
using namespace std;

int yak(int n1, int n2)
{
  int a{n1%n2};
  while(a!=0)
  {
    n1=n2;
    n2=a;
    a=n1%n2;
  }
  return n2;
}

int bae(int n1, int n2)
{
  int a{};
  a=(n1*n2)/yak(n1, n2);
  return a;
}

int main(void)
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int A{}, B{}, y{}, b{};
  cin>>A>>B;
  y=yak(A, B);
  b=bae(A, B);
  cout<<y<<"\n"<<b<<"\n";
}