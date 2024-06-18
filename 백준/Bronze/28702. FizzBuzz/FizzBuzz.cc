#include <iostream>
#include <string>
using namespace std;

int main(void)
{
  string str1{};
  string str2{};
  string str3{};
  int ans{0};
  cin>>str1;
  if(str1!="Fizz" && str1!="Buzz" && str1!="FizzBuzz")
    {
      ans=stoi(str1)+3;
    }
  cin>>str2;
  if(str2!="Fizz" && str2!="Buzz" && str2!="FizzBuzz")
    {
      ans=stoi(str2)+2;
    }
  cin>>str3;
  if(str3!="Fizz" && str3!="Buzz" && str3!="FizzBuzz")
    {
      ans=stoi(str3)+1;
    }
  
  if(ans%3==0 && ans%5==0)
    {
      cout<<"FizzBuzz";
    }
  else if(ans%3==0)
    {
      cout<<"Fizz";
    }
  else if(ans%5==0)
    {
      cout<<"Buzz";
    }
  else
    {
      cout<<ans;
    }
}