#include <string>
#include <vector>

using namespace std;

bool judge(int x)
{
    if(x%3==0) return false;
    string s=to_string(x);
    for(char c : s)
        if(c=='3')
            return false;
    return true;
}

int solution(int n)
{
    int answer=0;

    int digit=0;
    for(int i=1; i<=n; i++)
    {
        digit++;
        while(judge(digit)==false)
            digit++;
    }
    answer=digit;

    return answer;
}