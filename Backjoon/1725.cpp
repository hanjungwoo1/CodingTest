#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;

int N, ans, h[100002];
stack<int> s;

int main() 
{
	cin >> N;

	for (int i = 1; i <= N; i++) cin >> h[i];

	s.push(0);
	for (int i = 1; i <= N + 1; i++)
	{

		while (!s.empty() && h[s.top()] > h[i])
		{
			int check = s.top();
			s.pop();
			ans = max(ans, h[check]*(i - s.top() - 1));
		}
		s.push(i);
	}
	cout << ans;
	
}
